import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
count = 0

coins = [int(input()) for _ in range(N)]

coins.sort(reverse=True)

for coin in coins:
  count += K // coin
  K = K % coin
  if K == 0: break

print(count)