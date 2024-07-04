import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
Narr = list(map(int, input().rstrip().split()))

Narr.sort()
print(Narr[K-1])