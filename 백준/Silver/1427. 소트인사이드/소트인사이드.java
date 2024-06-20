import java.util.Scanner;
public class Main{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		String s;
		int N;
		int[] arr;
		//글자 1개 단어를 읽음.문제에서 숫자는 연속글자로 제공
		//   "2143"
		s = sc.next(); //"2143"
		N = s.length();// 문자열의 길이 -> 4
		arr = new int[N];
		for (int i = 0; i < N; i++) {
			//글자내 일부글자 추출
			// i에서 i+1미만 까지 문자열 추출
			String ss = s.substring(i,i+1);
			arr[i] = Integer.parseInt(ss); // "2" -> 2
		}
		// i는 최대값을 넣는 자리
		for (int i = 0; i < N; i++) { //2143
			//내림차순이기에 최대값의 위치를검색
			int max = i;//맨처음을 최대값으로 임의로 지정
			for (int j = i+1; j < N; j++) {
				if(arr[j] > arr[max]) {
					max = j;
				}
			}
			int tmp = arr[i];
			arr[i] = arr[max];
			arr[max] = tmp;
		}
		for (int i = 0; i < N; i++) {
			System.out.print(arr[i]);
		}
	}
}