import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 행/열 길이
graph = []  # 2차원 리스트의 맵 정보 저장할 공간
for _ in range(n):
    graph.append(list(input()))

def dfs(x, y):
    if graph[x][y] == '-':
        graph[x][y] = 1 # 해당 좌표 방문 처리
        for _y in [1, -1]:  # 좌우 확인
            Y = y + _y
            if 0 <= Y < m and graph[x][Y] == '-': # 범위 안에 있고 - 모양이라면
                dfs(x, Y) # 해당 좌표부터 dfs 탐색 재귀
    if graph[x][y] == '|':
        graph[x][y] = 1 
        for _x in [1, -1]: # 상하 확인
            X = x + _x
            if 0 <= X < n and graph[X][y] == '|':
                dfs(X, y)

cnt = 0
for i in range(n): # 이중 for문으로 모든 좌표 검사
  for j in range(m):
    if graph[i][j] == '-' or graph[i][j] == '|':
      dfs(i,j)
      cnt += 1 

print(cnt) # 바닥 모양 종류 개수