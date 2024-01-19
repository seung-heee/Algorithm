def solution(arr, flag):
    answer = []
    for i, value in enumerate(flag):
        if value:
            answer += [arr[i]] * arr[i] * 2
        else:
            answer = answer[: -arr[i]]
    return answer
