import sys

N, M = map(int, sys.stdin.readline().split())

arrA = []
arrB = []

for _ in range(N):
    arrA.append(list(map(int, sys.stdin.readline().split()))) # 행렬A

for _ in range(N):
    arrB.append(list(map(int, sys.stdin.readline().split()))) # 행렬B

for i in range(N):
    for j in range(M):
        res = arrA[i][j] + arrB[i][j]
        print(res, end=' ')
    print()
