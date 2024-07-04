import sys
input = sys.stdin.readline

N = int(input())
serial_number = []
serial_sum = dict()

for i in range(N):
  serial_number.append(input().rstrip())

for i in serial_number:
  temp = 0
  for j in i:
    if j.isdigit():
      temp += int(j)
  serial_sum[i] = temp

# 1. 길이가 짧은 것부터 정렬
# 2. 숫자만 비교 후 작은 합 먼저 정렬
# 3. 사전순 정렬
serial_number.sort(key = lambda x: (len(x), serial_sum[x], x))

for i in serial_number:
  print(i)
