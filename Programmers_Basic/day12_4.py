def solution(arr):
    answer = []
    idx_range = [idx for idx, value in enumerate(arr) if value == 2]
    min_range = min(idx_range, default=-1)
    max_range = max(idx_range, default=-1)
    
    return arr[min_range:max_range+1] if arr[min_range:max_range+1] else [-1]