import sys

N = int(sys.stdin.readline())
print(*[i for i in range(1, N+1)], sep='\n')