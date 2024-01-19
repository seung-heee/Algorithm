def solution(arr, k):
    answer = []
    newarr = []
    for i in arr:
        if i not in newarr:
            newarr.append(i)

    for i in range(k):
        try:
            answer.append(newarr[i])
        except:
            answer.append(-1)
    return answer
