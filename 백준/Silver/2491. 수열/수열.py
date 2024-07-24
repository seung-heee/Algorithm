import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

down, up = [1]*N, [1]*N

for i in range(1, N):
    if arr[i] <= arr[i-1]:
        down[i] = max(down[i], down[i-1]+1)
    if arr[i] >= arr[i-1]:
        up[i] = max(up[i], up[i-1]+1)
print(max(max(down), max(up)))