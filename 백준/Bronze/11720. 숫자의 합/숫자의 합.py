import sys

N = int(input())
num = int(input())

new = [int(i) for i in str(num)] 
print(sum(new))