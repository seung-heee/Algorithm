def solution(arr):
    int2 = [2**i for i in range(0, 12)]

    while len(arr) not in int2:
        arr.append(0)

    return arr
