import java.util.Scanner;

public class triangle {
	public static void main(String[] args) {
		Scanner sc = new Scanner (System.in);
		System.out.print("Enter the number: ");
		int num= sc.nextInt();
		num=num+1;
		for(int i=0; i<num; i++) {
			
			for (int j=0; j<num-i;j++)
			{
				System.out.print("  ");
			}
			
			for (int k=0; k<i; k++) {
				System.out.print("*");
				System.out.print("   ");
			}
			System.out.println();
		}
	}
}
