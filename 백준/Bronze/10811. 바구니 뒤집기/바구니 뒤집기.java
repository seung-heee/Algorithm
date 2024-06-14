import java.util.*;
public class Main{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int[] arr = new int[N+1];
		
		for (int i = 1; i <= N; i++) {
			arr[i] = i;
		}
		
		for (int i = 0; i < M; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			for (int j = a; j <= b; j++) {
				int bb = b--;
				int temp;
				
				temp = arr[j];
				arr[j] = arr[bb];
				arr[bb] = temp;
			}
		}
		
		for (int i = 1; i <= N; i++) {
			System.out.println(arr[i]);
		}
	}
}