import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.rmi.*;  
import java.rmi.server.*;  

public class SepolicyRemote extends UnicastRemoteObject implements Sepolicy{  
	SepolicyRemote()throws RemoteException{  
		super();  
	}
	public ArrayList<String> rules = new ArrayList<String>();
	
	public ArrayList<String> getDenials(String filename){
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
	
		
	public void resolveDenial(String denial){
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
		System.out.println("Resolving: " + scon + "by giving perm: " + per);
		String rule = "allow " + scon + " " + tcon + ":" + tcl + " { " + per + " };";
		if (!rules.contains(rule))
			rules.add(rule);
	}
	
	public ArrayList<String> getRules(ArrayList<String> denials){
		for( String denial : denials)
			resolveDenial(denial);
		return rules;
	}
	
}