import java.util.*;
public class Main{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
		int B = sc.nextInt();
		int C = sc.nextInt();
		int BC = B + C;
		
		while(BC > 59) {
			if (A<23) {
				A++;
				BC -= 60;
			} else {
				A = 0;
				BC -= 60;
			}
		}
		System.out.print(A + " " + BC);
	}
}