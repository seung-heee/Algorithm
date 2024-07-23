def fibo(n):
    if n <= 1:
        p[n] = n
        return n
    
    if p[n] == 0:
        p[n] = fibo(n-1) + fibo(n-2)
    return p[n]

p = [0] * 46
print(fibo(int(input())))