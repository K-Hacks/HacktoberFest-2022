package exp03;
import java.util.Scanner;
public class P6charrepeatcompress {
	public static void main(String[] args) {
		Scanner sc= new Scanner (System.in);
		System.out.println("Enter your string: ");
		String sen = sc.nextLine()+" ";
		String outsen="";
		char [] charc= sen.toCharArray();
		int temp=1;
		for(int i =0; i<charc.length-1;i++) {
			
			if(charc[i]==charc[i+1]) {
				temp=temp+1;
			}
			else {
				outsen=outsen+""+charc[i]+""+temp+"";
				temp=1;
			}
		}
		sc.close();
		System.out.println(outsen);
		
	}
}
