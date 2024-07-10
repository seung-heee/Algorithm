import sys
input = sys.stdin.readline

N = int(input())
number = list(map(int, input().rstrip().split()))
cnt = 0

for num in number:
  if num == 1: continue

  for j in range(2, num):
    if num % j == 0:
      break
  
  else:
    cnt += 1
  
print(cnt)