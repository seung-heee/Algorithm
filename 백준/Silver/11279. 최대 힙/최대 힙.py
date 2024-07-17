import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
  x = int(input())
  if x == 0:
    if not heap:
      print(0)
    else:
      maxItem = heapq.heappop(heap)[1]
      print(maxItem)
  else:
    heapq.heappush(heap, (-x, x))