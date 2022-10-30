import java.util.Scanner;

public class pattern1 {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.print("Enter a number less than 8: ");
		int num = sc.nextInt();
		
		if(num>7)
			num=7;
		
		for(int i=0; i<num; i++) {
			for(int j=0; j<=(i); j++) {
				System.out.print("*");
			}
			System.out.println();
		}
		
		
		sc.close();
	}
}
