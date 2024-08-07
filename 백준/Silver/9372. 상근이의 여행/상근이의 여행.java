import java.util.Scanner;

public class Main {
	public static int T; // 테스트 케이스 개수
	public static int n, m; // 나라 n개, 비행기 m
	public static int[] parent = new int[1000001]; // 부모 테이블 초기화하기
    public static int result = 0;
    
    // 특정 원소가 속한 집합을 찾기
    public static int findParent(int x) {
        // 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
        if (x == parent[x]) return x;
        return parent[x] = findParent(parent[x]);
    }

    // 두 원소가 속한 집합을 합치기
    public static void unionParent(int a, int b) {
        a = findParent(a);
        b = findParent(b);
        if (a < b) parent[b] = a;
        else parent[a] = b;
    }

	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        T = sc.nextInt();
        for (int t = 0; t < T; t++) {
            result = 0;
            n = sc.nextInt();
            m = sc.nextInt();
            
            // 부모 테이블상에서, 부모를 자기 자신으로 초기화
            for (int i = 1; i <= n; i++) {
                parent[i] = i;
            }
            
            for (int i = 0; i < m; i++) {
                int a = sc.nextInt();
                int b = sc.nextInt();
				
                if (findParent(a) != findParent(b)) {
                    unionParent(a, b);
                    result++;
                }
			}
            System.out.println(result);
		}
	}

}
