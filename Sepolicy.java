import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.rmi.*;  

public interface Sepolicy extends Remote{  
	public ArrayList<String> rules = new ArrayList<String>();	
	public ArrayList<String> getDenials(String filename) throws RemoteException;
	public void resolveDenial(String denial) throws RemoteException;
	
	public ArrayList<String> getRules(ArrayList<String> denials) throws RemoteException;	
}