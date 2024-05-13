A = int(input())
B = int(input())
C = int(input())

N = str(A*B*C)

for i in '0123456789':
  print(N.count(i))