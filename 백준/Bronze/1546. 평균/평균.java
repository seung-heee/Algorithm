import java.util.*;
public class Main{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		double M = 0;
		double sum = 0;
		double[] Narr = new double[N];
		double[] newArr = new double[N];
		
		for (int i = 0; i < N; i++) {
			Narr[i] = sc.nextInt();
			if (Narr[i] > M) M = Narr[i];
		}
		
		for (int i = 0; i < Narr.length; i++) {
			newArr[i] = Narr[i] / M * 100;
			sum += newArr[i];
		}
		System.out.println(sum/N);
	}
}