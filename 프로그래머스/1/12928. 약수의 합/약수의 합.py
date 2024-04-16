def solution(n):
    sumV = 0
    sumV = sum([i for i in range(1, n+1) if n % i == 0])
    return sumV
