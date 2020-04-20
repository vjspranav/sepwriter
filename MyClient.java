import java.util.ArrayList;
import java.rmi.*;  
import java.io.FileWriter;
import java.io.File;
import java.io.IOException;
// For GUI
import java.applet.*;
import java.awt.*;
import javax.swing.*; 
import java.awt.event.*;
//For Status
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

public class MyClient{  
	public static void main(String args[]){
		new GUI();
	}  
}

class GUI extends JFrame implements ActionListener {
	public static int connected=0;
	public static boolean rulesset=false;
	public static ArrayList<String> rules;
	JFrame f=new JFrame();
	JLabel l1=new JLabel("Path to your logcat file: ");
	JLabel l2=new JLabel("Path your Device Tree: ");
	JLabel l3=new JLabel("Your denials are located at: ");	
	public static JLabel status = new JLabel("Device Status: ", JLabel.CENTER);
	public static JTextField t1=new JTextField(20);
	public static JTextField t2=new JTextField(20);
	public static JTextField t3=new JTextField(20);
	public static JButton b1=new JButton("Get Denials");
	public static JButton b2=new JButton("Get Logs");
	public static JButton b5=new JButton("Write to tree");
	JButton b3=new JButton("Browse");
	JButton b4=new JButton("Browse");
	JPanel p1 = new JPanel(new GridLayout(3, 2, 4, 2)); 
	JPanel p2 = new JPanel();
	JPanel p3 = new JPanel();
	JFileChooser fc = new JFileChooser();
	GUI(){
		p2.setLayout(new FlowLayout());
		p3.setLayout(new FlowLayout());
		p1.add(l1);
		p1.add(t1);
		p1.add(b3);
		p1.add(l2);		
		p1.add(t2);
		p1.add(b4);
		p1.add(l3);		
		p1.add(t3);
		p1.add(b5);
		p2.add(b1);
		p2.add(b2);
		p3.add(status);
		b1.addActionListener(this);
		b2.addActionListener(this);
		b3.addActionListener(this);
		b4.addActionListener(this);
		b5.addActionListener(this);
		t3.setEditable(false); 
		f.add(p1, "North"); 
		f.add(p2);
		f.add(p3, "South");
		f.setVisible(true);
		f.setSize(500,200);
		b1.setEnabled(false);
		b2.setEnabled(false);
		b5.setEnabled(false);
		ScheduledExecutorService executorService = Executors.newSingleThreadScheduledExecutor();
		executorService.scheduleAtFixedRate(GUI::run, 0, 1, TimeUnit.SECONDS);
	}
	private static void run() {
		int count=0;
		try {
			Process process = Runtime.getRuntime().exec("adb devices");
			BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
			String line;
			line = reader.readLine();
			while ((line = reader.readLine()) != null) {
 				if(line.contains("device"))
					count++;			
			}
		} catch (IOException e) { System.out.println(e); }
		if(count==0){
			status.setText("Device Status: Disconnected");
			connected=0;
			status.setForeground(Color.red);
			b2.setEnabled(false);
		}else if(count==1){
			status.setText("Device Status: Connected");
			connected=1;
			status.setForeground(Color.green);
			b2.setEnabled(true);
		}else if(count>1){
			status.setText("Device Status: " + count + " devices Connected");
			connected=0;			
			status.setForeground(Color.red);
			b2.setEnabled(false);
		}
		File tmp = new File(t1.getText());
		if( tmp.exists() && !tmp.isDirectory())
			b1.setEnabled(true);
		else
			b1.setEnabled(false);
		tmp = new File(t2.getText());
		if( tmp.exists() && tmp.isDirectory() && rulesset)
			b5.setEnabled(true);
		else
			b5.setEnabled(false);
	}
	
	public void actionPerformed(ActionEvent e){
		if(e.getSource()==b1){
			String s1 = t1.getText();
			if(s1.contains("\\"))
			s1 = s1.replaceAll("\\\\", "/");
			String fname = s1.substring(0,s1.lastIndexOf("/")) + "/Rules.txt";
			try{  
				FileWriter writer = new FileWriter(fname);
				Sepolicy resolver=(Sepolicy)Naming.lookup("rmi://localhost:5000/jp_rmi");  
				ArrayList<String> denials = resolver.getDenials(s1);
				rules = resolver.getRules(denials);	  
				for( String rule : rules){
					System.out.println("in " + rule.split(" ", 0)[1] + ".te\n" + rule);
					writer.write("in " + rule.split(" ", 0)[1] + ".te\n" + rule + "\n");
				}
				writer.close();
				}catch(Exception ex){}				
			t3.setText("Stored at " + fname);
			Runtime runtime = Runtime.getRuntime();
			try{    
				runtime.exec("notepad.exe " + fname);
			}catch(IOException ex){}
			rulesset=true;
		}else if(e.getSource()==b2){
			int denial=0;
			try{
				Process process = Runtime.getRuntime().exec("adb shell dmesg");
				BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
				String line;
				FileWriter writer = new FileWriter("log.txt");
				while ((line = reader.readLine()) != null){ 
					if(line.contains("avc:"))
						denial=1;
					writer.write(line + "\n");
				}
				writer.close();
				if(denial==1){
					t1.setText("log.txt");
					JOptionPane.showMessageDialog(f, "Please Press on Get Denials");
				}else{
					JOptionPane.showMessageDialog(f, "No Denial in log");
				}
			}catch(IOException ex){}
		}else if(e.getSource()==b3){
			fc.setFileSelectionMode(JFileChooser.FILES_ONLY);
			int returnVal = fc.showOpenDialog(GUI.this);
			if (returnVal == JFileChooser.APPROVE_OPTION) {
				t1.setText(fc.getSelectedFile().getPath());
			}
		}else if(e.getSource()==b4){
			fc.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);
			int returnVal = fc.showOpenDialog(GUI.this);
			if (returnVal == JFileChooser.APPROVE_OPTION) {
				t2.setText(fc.getSelectedFile().getPath());
			}
		}
	}
}