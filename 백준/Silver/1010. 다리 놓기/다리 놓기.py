import sys
t = int(sys.stdin.readline())

for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    if n == m:
        print(1)
    else:
        ans = 1
        for i in range(m, m-n, -1):
            ans *= i
        for j in range(n, 1, -1):
            ans = ans // j
        print(ans)