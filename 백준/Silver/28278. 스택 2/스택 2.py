import sys
input = sys.stdin.readline

N = int(input()) # 명령의 수
arr = []

for i in range(N):
  cmd = input().split()
  c = int(cmd[0])

  if c == 1:
    arr.append(cmd[1])

  elif c == 2:
    if not arr:
      print(-1)
    else: 
      print(arr.pop())

  elif c == 3:
    print(len(arr))

  elif c == 4:
    if not arr:
      print(1)
    else: 
      print(0)

  elif c == 5:
    if not arr:
      print(-1)
    else:
      print(arr[-1])