import java.util.*;
public class Main{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int X = sc.nextInt();
		int[] Aarr = new int[N];
		
		for (int i = 0; i < N; i++) {
			int a = sc.nextInt();
			Aarr[i] = a;
		}
		
		for (int i = 0; i < Aarr.length; i++) {
			if (Aarr[i] < X) System.out.println(Aarr[i]);
		}
		
	}
}