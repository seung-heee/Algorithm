import sys

T = int(sys.stdin.readline())
res = []

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    res.append(A+B)

print(*res, sep='\n')