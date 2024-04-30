import sys

N = int(sys.stdin.readline())

def fact(n):
  if n < 1:
    return 1
  return n * fact(n-1)

print(fact(N))