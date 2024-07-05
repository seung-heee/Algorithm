import sys
input = sys.stdin.readline

num = []
for i in range(5):
  num.append(int(input()))

num.sort()
mid = len(num) // 2 # 중앙 인덱스 번호
sum = sum(num)

print(sum // len(num)) # 평균
print(num[mid]) # 중앙값
