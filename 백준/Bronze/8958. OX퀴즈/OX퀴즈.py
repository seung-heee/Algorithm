T = int(input())

for _ in range(T):
  sum = 0
  temp = 0
  S = input()

  for i in S:
    if i == 'O':
      temp += 1
      sum += temp
    else:
      temp = 0
  print(sum)