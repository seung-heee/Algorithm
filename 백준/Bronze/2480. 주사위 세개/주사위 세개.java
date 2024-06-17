import java.util.*;
public class Main{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
		int B = sc.nextInt();
		int C = sc.nextInt();
        int[] arr = {A, B, C};
		
		if (A==B && A==C) System.out.println(10000+(A)*1000);
		else if (A==B || A==C || B==C) {
			if (A==B || A==C) System.out.println(1000+(A)*100);
			else System.out.println(1000+(B)*100);
		} else {
			Arrays.sort(arr);
			System.out.println((arr[2])*100);
		} 
	}
}