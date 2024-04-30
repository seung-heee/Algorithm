import sys

T = int(sys.stdin.readline())
res = []

for _ in range(T):
  A, B = map(int, sys.stdin.readline().split())
  print(A + B)
