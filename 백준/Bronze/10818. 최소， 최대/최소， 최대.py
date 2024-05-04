import sys

N = int(input())
N_list = list(map(int, sys.stdin.readline().split()))

print(f'{min(N_list)} {max(N_list)}')