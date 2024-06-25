import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []

for i in range(1, N+1):
  arr.append(i)

for i in range(M):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  temp = arr[a]
  arr[a] = arr[b]
  arr[b] = temp

print(' '.join(map(str, arr)))