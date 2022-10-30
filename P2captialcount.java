package exp03;
import java.util.Scanner;
public class P2captialcount {
	public static void main(String[] args) {
		Scanner sc= new Scanner (System.in);
		System.out.println("Enter your string: ");
		String sen = sc.nextLine();
		sen = sen.trim();
		char cap[]= new char[sen.length()];
		int capi=0;
		char sap[]= new char[sen.length()];
		int sapi=0;
		
		int flag=0;
		
		for(int i=0;i<sen.length() ;i++) {
			if(sen.charAt(i)>=65 && sen.charAt(i)<=90 &&sen.charAt(i)!=32) {
				for(int c=0; c<=capi;c++) 
					if(cap[c] == sen.charAt(i)) {
						flag=1;
					}
				if(flag==0) {
					cap[capi]=sen.charAt(i);
					capi=capi+1;
				}
				if(flag==1)
					flag=0;
				
			}
			if(sen.charAt(i)>=97 && sen.charAt(i)<=122 &&sen.charAt(i)!=32) {
				for(int c=0; c<=sapi;c++) 
					if(sap[c] == sen.charAt(i)) {
						flag=1;
					}
				if(flag==0) {
					sap[sapi]=sen.charAt(i);
					sapi=sapi+1;
				}
				if(flag==1)
					flag=0;
				
			}
		}
		
		System.out.print("There are "+(capi)+" capital letters : ");
		for(int i=0;i<capi;i++)
			System.out.print(cap[i]);
		System.out.println();
		
		System.out.print("There are "+(sapi)+" small letters : ");
		for(int i=0;i<sapi;i++)
			System.out.print(sap[i]);
		System.out.println();
		sc.close();
	}
}
