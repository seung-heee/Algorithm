import sys

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

minArr = [i for i in A if i < X]
print(*minArr)