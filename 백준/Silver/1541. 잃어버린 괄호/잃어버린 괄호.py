import sys
input = sys.stdin.readline

exp = input().rstrip().split('-') 
arr = []

for i in range(len(exp)):
  temp = 0  
  for t in exp[i].rstrip().split('+'):
    temp += int(t)
  arr.append(temp)

res = arr[0]
for a in arr[1:]:
  res -= a

print(res)