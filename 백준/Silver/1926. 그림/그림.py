# 1. 아이디어
# - 2중 for => 값 1 && 방문 X => BFS
# - BFS 돌면서 그림 개수 +1, 최대값 갱신

# 2. 자료구조
# - 그래프 전체 지도 : [][]
# - 방문 : bool[][]
# - Queue(BFS)

import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 행,열 개수
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0 ,-1, 0]

def bfs(y, x):
  rs = 1 # 그림 크기 저장 변수
  q = [(y, x)]
  while q: # q가 빌 때 까지
    ey, ex = q.pop() # 해당 좌표 꺼내서
    for k in range(4): # 상하좌우 탐색
      ny = ey + dy[k]
      nx = ex + dx[k]
      if 0<=ny<n and 0<=nx<m: # 좌표가 그래프 범위 내에 있고
        if map[ny][nx] == 1 and chk[ny][nx] == False: # 그림이고, 방문하지 않았을 때
          rs += 1 # 그림 크기 +1
          chk[ny][nx] = True # 방문여부 표시
          q.append((ny, nx)) # 큐에 새로운 좌표 추가
  return rs

cnt = 0 # 그림 개수
maxv = 0 # 최대 그림 크기

for j in range(n):
  for i in range(m):
    if map[j][i] == 1 and chk[j][i] == False:
      # 방문한 곳 True로 변경
      chk[j][i] = True
      # 전체 그림 갯수를 +1
      cnt += 1
      # BFS > 그림의 크기를 구해주고 최대값 갱신
      maxv = max(maxv, bfs(j, i))

print(cnt)
print(maxv)
