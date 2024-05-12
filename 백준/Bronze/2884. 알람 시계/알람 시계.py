import sys

H, M = map(int, sys.stdin.readline().split())

if M >= 45:
  print(H, M-45)
else:
  if (H == 0):
    M = 60 - abs(M-45)
    print(23, M)
  else:
    M = 60 - abs(M-45)
    print(H-1, M)