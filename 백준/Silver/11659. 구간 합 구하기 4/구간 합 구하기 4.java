import java.util.*;
public class Main{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int[] Narr = new int[N+1];
		int res = 0;
		
		for (int i = 0; i < N; i++) {
			int a = sc.nextInt();
			Narr[i+1] = Narr[i] + a;
		}
		
		for (int i = 0; i < M; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			res = Narr[b] - Narr[a-1];
			System.out.println(res);
			res = 0;
		}
	}
}