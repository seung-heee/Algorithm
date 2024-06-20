import java.util.*;
public class Main{
	static void swap(int[] a, int idx1, int idx2) {
		int t = a[idx1];
		a[idx1] = a[idx2];
		a[idx2] = t;
	}
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] a = new int[N];
        
        for (int i = 0; i < N; i++) {
        	a[i] = sc.nextInt();
        }
        
        for (int i = 0; i < N - 1; i++) {
			for (int j = N - 1; j > i; j--) {
				if(a[j-1] > a[j]) swap(a, j-1,j);
			}
		}
        
        for (int i = 0; i < a.length; i++) {
        	System.out.println(a[i]);
		}
    }
}