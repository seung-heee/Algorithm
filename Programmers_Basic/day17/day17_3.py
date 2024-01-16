def solution(strArr):
    answer = []
    for idx, value in enumerate(strArr):
        if "ad" not in value:
            answer.append(strArr[idx])

    return answer
