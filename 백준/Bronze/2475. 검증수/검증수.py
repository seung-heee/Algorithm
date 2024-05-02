import sys

num = list(map(int, sys.stdin.readline().split()))
res = sum([i * i for i in num]) % 10
print(res)