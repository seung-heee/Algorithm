import sys
input = sys.stdin.readline

K = int(input())

# K = 1 2 3 4 5 6 7 8
# a = 0 1 1 2 3 5 8 11
# b = 1 1 2 3 5 8 11

a = [0] * 46
b = [0] * 46

a[0] = 1
a[1] = 0

b[0] = 0
b[1] = 1

for i in range(2, 46):
  a[i] = a[i-1] + a[i-2]
  b[i] = b[i-1] + b[i-2]

print(a[K], b[K])