import sys
input = sys.stdin.readline

N = int(input())
time = [*map(int, input().split())]
time.sort() # 인출하는 시간이 짧은 사람 먼저 줄세우기 
sum = 0

for i in range(len(time)):
  sum += time[i] 
  time[i] = sum # 앞 사람 시간 + 내 시간 => i번째 사람이 걸리는 시간

sum = 0

for T in time:
  sum += T # N명의 사람이 총 걸리는 시간의 최솟값

print(sum)