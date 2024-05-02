import sys

A, B = map(int, sys.stdin.readline().split())

def num(a,b):
  res = (a+b)*(a-b)
  print(res)

num(A, B)