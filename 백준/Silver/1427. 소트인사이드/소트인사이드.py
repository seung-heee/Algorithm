import sys
input = sys.stdin.readline

N = input().rstrip()
arr =[]

for i in N:
  arr.append(int(i))

sortArr = sorted(arr, reverse=True)
print(''.join(map(str, sortArr)))