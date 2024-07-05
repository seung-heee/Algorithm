import sys
input = sys.stdin.readline

A, B, C = map(int, input().rstrip().split())
arr = []

arr.append(A)
arr.append(B)
arr.append(C)

arr.sort()

print(arr[-2])