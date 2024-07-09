import sys
input = sys.stdin.readline

A, B, N = map(int, input().rstrip().split())
# 런타임 에러
# res = str(A / B).split('.')[1]
# print(res[N-1])

for i in range(N):
  A = (A % B) * 10
  res = A // B

print(res)