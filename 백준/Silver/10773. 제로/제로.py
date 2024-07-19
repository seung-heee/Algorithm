import sys
input = sys.stdin.readline

K = int(input())
arr = []

for _ in range(K):
  num = int(input())
  if not num:
    arr.pop()
  else:
    arr.append(num)

print(sum(arr))