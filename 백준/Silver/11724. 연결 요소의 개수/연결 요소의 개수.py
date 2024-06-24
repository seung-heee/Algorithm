import sys
input = sys.stdin.readline
from collections import defaultdict

sys.setrecursionlimit(10**7)
def dfs(v):
  visited[v] = True
  for i in graph[v]:
    if visited[i] == False:
      dfs(i)


# 정점의 개수 N, 간선의 개수 M
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

# 간선의 양 끝점 u,v - M개 주어짐
for _ in range(M):
  u, v = map(int, input().split())
  graph[u].append(v) 
  graph[v].append(u)

visited = [False] * (N + 1) # 방문처리
count = 0

for i in range(1, N+1):
  if visited[i] == False: # i번째 노드를 방문하지 않았다면
    count += 1
    dfs(i)

print(count)

