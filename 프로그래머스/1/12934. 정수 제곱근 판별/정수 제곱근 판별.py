import math

def solution(n):
    answer = int(n**0.5)
    if answer ** 2 == n:
        return (answer+1) ** 2
    else: return -1