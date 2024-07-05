import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().rstrip().split()))
B = list(map(int, input().rstrip().split()))

S = 0
for i in range(N):
  S += min(A) * max(B)
  A.pop(A.index(min(A)))
  B.pop(B.index(max(B)))

print(S)