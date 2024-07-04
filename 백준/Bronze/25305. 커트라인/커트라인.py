import sys
input = sys.stdin.readline

N, k = map(int, input().rstrip().split())
score = list(map(int, input().rstrip().split()))

score.sort()

print(score[-k])