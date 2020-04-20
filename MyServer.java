import java.rmi.*;  
import java.rmi.registry.*;  
public class MyServer{  
	public static void main(String args[]){  
		try{  
			Sepolicy resolver=new SepolicyRemote();  
			Naming.rebind("rmi://localhost:5000/jp_rmi",resolver);  
		}catch(Exception e){System.out.println(e);}  
	}  
}  