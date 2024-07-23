import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def fibo(n):
    if n <= 1:
        p[n] = n
        return n
    
    if p[n] == 0:
        p[n] = fibo(n-1) + fibo(n-2)
    return p[n]

p = [0] * 10001
print(fibo(int(input())))