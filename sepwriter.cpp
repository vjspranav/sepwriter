#include<iostream>
#include<String.h>
#include <iostream>
#include <fstream>
#include <sstream>

int no;
using namespace std;

void getdenials(string logcat){
	ifstream file("logcat.txt");
	ofstream den("denials.txt");
	string line;
	while (getline(file, line)){
		if(line.size() > 0 && line.find("avc:")!= string::npos){
			den << line << endl;
			no+=1;
		}
	}	
}

string get_str_between_two_str(const string &s, const string &start_delim, const string &stop_delim){
    unsigned first_delim_pos = s.find(start_delim);
    unsigned end_pos_of_first_delim = first_delim_pos + start_delim.length();
    unsigned last_delim_pos = s.find_first_of(stop_delim, end_pos_of_first_delim);

    return s.substr(end_pos_of_first_delim,
            last_delim_pos - end_pos_of_first_delim);
}

int main(){
	ifstream den("denials.txt");
	ofstream res("res.txt");
	string words[20];
	string line, ss;
	string per, scon, tcon, tcl;
	int n;
	while (getline(den, line)){
		if(line.size() > 0){
		    n=0;
			per = get_str_between_two_str(line, "{", "}");
			scon = get_str_between_two_str(line, "scontext=u:r:", " ");
		    while(scon.substr( scon.length() - 3 ) != ":s0")
			    scon = scon.substr(0, scon.size()-1);
		    scon = scon.substr(0, scon.size()-3);
			if(line.find("tcontext=u:r:")!= string::npos){
				tcon = get_str_between_two_str(line, "tcontext=u:r:", " ");
			    while(tcon.substr( tcon.length() - 3 ) != ":s0")
	    			tcon = tcon.substr(0, tcon.size()-1);
			    tcon = tcon.substr(0, tcon.size()-3);
			}
			if(line.find("tcontext=u:object_r:")!= string::npos){
				tcon = get_str_between_two_str(line, "tcontext=u:object_r:", " ");
			    while(tcon.substr( tcon.length() - 3 ) != ":s0")
	    			tcon = tcon.substr(0, tcon.size()-1);
			    tcon = tcon.substr(0, tcon.size()-3);
			}
			tcl = get_str_between_two_str(line, "tclass=", " ");
			res << "allow " << scon << " " << tcon << ":" << tcl << " {" << per << "}" << endl;
		}
	}
}
