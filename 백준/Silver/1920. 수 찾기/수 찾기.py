import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
arr = list(map(int, input().split()))
isTrue = True

for key in arr:
  pl = 0
  pr = N - 1
  isTrue = False

  while (pl <= pr):
    pc = (pl + pr) // 2
    if key == A[pc]:
      print(1)
      isTrue = True
      break
    elif (key < A[pc]):
      pr = pc - 1
    else:
      pl = pc + 1
  if not isTrue: print(0)