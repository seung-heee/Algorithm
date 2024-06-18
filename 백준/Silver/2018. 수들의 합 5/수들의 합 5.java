import java.util.*;
public class Main{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int sum = 0;
		int cnt = 0;
		
		for (int i = 1; i <= N; i++) {
			for (int j = i; j <= N; j++) {
				sum += j;
				if (sum == N) {
					cnt++;
					sum = 0;
					break;
				} else if (sum > N) {
					sum = 0;
					break;
				}
			}
		}
		System.out.println(cnt);
	}
}