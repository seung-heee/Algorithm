import java.util.*;
public class Main{
	public static void main(String args[]){
Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int M = sc.nextInt();
        
        int[][] Aarr = new int[N][M];
        int[][] Barr = new int[N][M];
        int[][] newArr = new int[N][M];
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                Aarr[i][j] = sc.nextInt();
            }
        }
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                Barr[i][j] = sc.nextInt();
            }
        }
        
		sc.close();
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                newArr[i][j] = Aarr[i][j] + Barr[i][j];
            }
        }
        
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                System.out.print(newArr[i][j] + " ");
            }
            System.out.println(); 
        }
	}
}