import sys
import math
from functools import reduce
from math import gcd

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().rstrip().split()))

# 소수를 판별하는 함수
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 소수 목록
prime_list = [i for i in arr if is_prime(i)]

# 최소공배수 계산
def lcm(a, b):
    return a * b // gcd(a, b)

# prime_list가 비어있는지 확인하고, 비어있다면 -1을 출력
if not prime_list:
    print(-1)
else:
    # reduce를 사용하여 prime_list의 최소공배수 계산
    result = reduce(lcm, prime_list)
    print(result)