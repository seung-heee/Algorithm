import java.util.*;
public class Main{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int X = sc.nextInt();
		int[] A = new int[N];
		
		for (int i = 0; i < A.length; i++) {
			int a = sc.nextInt();
			A[i] = a;
		}
		
		for (int i = 0; i < A.length; i++) {
			if(A[i] < X) System.out.println(A[i]);
		}
	}
}