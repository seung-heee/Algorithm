import sys

num = []
T = int(sys.stdin.readline())
for i in range(T):
  A, B = map(int, sys.stdin.readline().split())
  num.append(A+B)

print(*num, sep='\n')