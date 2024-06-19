import java.util.*;
public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[N];
        
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        int cnt = 0;
        int max_height = 0;
        
        // 오른쪽에서 왼쪽으로 순회하면서 보이는 막대기의 개수를 셈
        for (int i = N - 1; i >= 0; i--) {
            if (arr[i] > max_height) {
                cnt++;
                max_height = arr[i];
            }
        }
        
        System.out.println(cnt);
    }
}
