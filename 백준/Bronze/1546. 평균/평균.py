import sys

N = int(input())
scores = list(map(int, sys.stdin.readline().split()))
M = max(scores)
sum = 0

for i in range(N):
  sum += scores[i] / M * 100

print(sum / N)