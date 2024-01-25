def solution(a, b):
    oddA = a % 2 == 1
    oddB = b % 2 == 1

    if oddA and oddB:
        return a**2 + b**2
    elif oddA or oddB:
        return 2 * (a + b)
    else:
        return abs(a - b)
