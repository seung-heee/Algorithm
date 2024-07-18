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
      # minItem = heapq.heappop(heap)
      # print(minItem[1])

      _, min_value = heapq.heappop(heap)
      print(min_value)
  else:
      heapq.heappush(heap, (abs(x), x))