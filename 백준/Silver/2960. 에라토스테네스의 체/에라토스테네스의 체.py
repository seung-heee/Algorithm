import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

num = [False] * (N + 1)
num_cnt = []

def PrimeNum(N):
  for i in range(2, N + 1):
    if num[i]: 
      continue
    for j in range(i, N + 1, i):
      if num[j] == False:
        num[j] = True
        num_cnt.append(j)

PrimeNum(N)

print(num_cnt[K-1])