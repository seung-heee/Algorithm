def solution(arr):
    if len(arr) == 1:
        return [-1]
    minV = min(arr)
    return [i for i in arr if minV != i]
