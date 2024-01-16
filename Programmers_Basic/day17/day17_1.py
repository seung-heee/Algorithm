def solution(myString, pat):
    answer = myString[: myString.rindex(pat) + len(pat)]
    return answer
