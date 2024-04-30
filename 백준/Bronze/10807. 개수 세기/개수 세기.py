import sys

N = int(input())
arr = map(int, sys.stdin.readline().split())
v = int(input())

cnt = [1 for i in arr if i == v]
print(len(cnt))