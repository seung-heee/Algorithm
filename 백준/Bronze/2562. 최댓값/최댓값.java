import java.util.*;
public class Main{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		int[] arr = new int[9];
		int max = 0;
		int maxIndex = 0;
		
		for (int i = 0; i < 9; i++) {
			arr[i] = sc.nextInt();
		}
		
		for (int i = 0; i < arr.length; i++) {
			if (arr[i] > max) {
				max = arr[i];
				maxIndex = i;
			}
		}
		System.out.println(max);
		System.out.println(maxIndex + 1);
	}
}