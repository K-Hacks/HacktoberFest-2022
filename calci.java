import java.util.Scanner;
public class calci {
	public static void main(String[] args) {
		Scanner sc = new Scanner (System.in);
		System.out.print("Enter number 1: ");
		int n1=sc.nextInt();
		System.out.print("Enter number 2: ");
		int n2=sc.nextInt();
		System.out.print("Enter the operation: ");
		String op = sc.next();
		
		if(op.equals("+"))
			System.out.println("The sum is : "+(n1+n2));
		if(op.equals("-"))
			System.out.println("The sum is : "+(n1-n2));
		if(op.equals("/"))
			System.out.println("The sum is : "+(n1/n2));
		if(op.equals("*"))
			System.out.println("The sum is : "+(n1*n2));
		sc.close();
	}
}
