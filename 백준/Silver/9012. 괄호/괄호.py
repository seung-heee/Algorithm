import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  test = input()
  stack = []

  for t in test:
    if t == '(':
      stack.append(t)
    elif t == ')':
      if not stack:
        print('NO')
        break
      else:
        stack.pop()
  else:
    if not stack:
      print('YES')
    else:
      print('NO')