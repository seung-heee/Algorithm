import sys
input = sys.stdin.readline
from collections import defaultdict

sys.setrecursionlimit(10**7)

cnt = 1

def dfs(v):
  global cnt
  visited[v] = cnt
  for i in graph[v]:
    if not visited[i]:
      cnt += 1
      dfs(i)

# 정점의 개수 N, 간선의 개수 M
N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]

# 간선의 양 끝점 u,v - M개 주어짐
for _ in range(M):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

visited = [0] * (N + 1) # 방문처리

for i in range(N+1): # 오름차순으로 인접노드 방문하기 위해 정렬
    graph[i].sort()


# DFS 수행
dfs(R)


# 각 정점의 방문 순서 출력
for i in range(1, N+1):
    print(visited[i])
