import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;
import java.util.ArrayList;

public class Sepolicy{
	public static ArrayList<String> rules = new ArrayList<String>();
	
	public static ArrayList<String> getDenials(String filename){
		ArrayList<String> denials = new ArrayList<String>();
		try{
			File logfile = new File(filename);  
			Scanner myReader = new Scanner(logfile);
			while (myReader.hasNextLine()) {
				String data = myReader.nextLine();
				if(data.contains("avc:"))
					denials.add(data);
			}
			myReader.close();
		}catch (FileNotFoundException e) {
			System.out.println("An error occurred.");
			e.printStackTrace();
		}
		return denials;
	}
	
		
	public static void resolveDenial(String denial){
        String[] perm = denial.split(" ", 0);
		String scon = "", tcl = "" , per = "", tcon = "";
        for(int i=0;i<perm.length;i++){
			if(perm[i].compareTo("{") == 0)
				per = perm[i+1];
			if(perm[i].contains("scontext="))
				scon = (perm[i].split("u:r:", 0)[1]).split(":s0", 0)[0];
			if(perm[i].contains("tcontext=") && perm[i].contains("u:object_r:"))
				tcon = perm[i].split("u:object_r:")[1].split(":s0")[0];
			if(perm[i].contains("tcontext=") && perm[i].contains("u:r:"))
				tcon = perm[i].split("u:r:")[1].split(":s0")[0];
			if(perm[i].contains("tclass="))
				tcl = perm[i].split("tclass=")[1];
		}
		String rule = "allow " + scon + " " + tcon + ":" + tcl + " { " + per + " };";
		if (!rules.contains(rule))
			rules.add(rule);
	}
	
	public static ArrayList<String> getRules(ArrayList<String> denials){
		for( String denial : denials)
			resolveDenial(denial);
		return rules;
	}
	
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		System.out.print("Please enter the path of your log file: ");
		ArrayList<String> denials = getDenials(scan.nextLine());
		getRules(denials);
		for( String rule : rules)	
			System.out.println("in " + rule.split(" ", 0)[1] + ".te\n" + rule);
		}
}
