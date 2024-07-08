import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))

for i in range(1, min(arr)+1):
  flag = True
  for num in arr:
    if  num % i != 0:
      flag = False
      break
  if flag:
    print(i)