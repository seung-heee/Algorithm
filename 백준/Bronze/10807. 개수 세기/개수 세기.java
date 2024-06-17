import java.util.*;
public class Main{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] Narr = new int[N];
		int count = 0;
		
		for (int i = 0; i < N; i++) {
			int n = sc.nextInt(); 
			Narr[i] = n;
		}
		
		int v = sc.nextInt();
		
		for (int i = 0; i < Narr.length; i++) {
			if (Narr[i] == v) count++;
		}
		System.out.println(count);
	}
}