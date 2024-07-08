import sys
input = sys.stdin.readline

N = int(input())
res = N
cnt = 0

while True:
  a = N // 10
  b = N % 10
  c = (a + b) % 10
  N = (b * 10) + c

  cnt += 1
  if (res == N):
    break

print(cnt)