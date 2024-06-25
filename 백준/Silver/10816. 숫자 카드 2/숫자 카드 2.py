import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
Narr = list(map(int, input().split()))
Narr.sort()

M = int(input())
Marr = list(map(int, input().split()))
isTrue = False

# Counter를 사용하여 각 요소의 개수를 미리 셈
count_dict = Counter(Narr)
countArr = [0] * M

for i in range(M):
  pl = 0
  pr = N - 1

  while(pl <= pr):  
    pc = (pl + pr) // 2

    if (Marr[i] == Narr[pc]):
      countArr[i] = count_dict[Marr[i]]
      break
    elif (Marr[i] < Narr[pc]):
      pr = pc - 1
    else:
      pl = pc + 1

print(" ".join(map(str, countArr)))