import java.util.*;
public class Main{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
        int a;
        int[] arr = new int[10];
        int count = 0;

        for (int i = 0; i < 10; i++) {
            a = sc.nextInt();
            int value = a % 42;

            if (count > 0 && Arrays.stream(arr, 0, count).anyMatch(x -> x == value)) {
                continue;
            } else {
                arr[count] = value;
                count++;
            }
        }
        System.out.println(count); // 서로 다른 값이 몇 개 있는지 출력
	}
}