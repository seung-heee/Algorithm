def solution(picture, k):
    answer = []
    for i in picture:
        temp = ""

        for j in i:
            temp += j * k

        for _ in range(k):
            answer.append(temp)
    return answer
