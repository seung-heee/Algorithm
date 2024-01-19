def solution(myStr):
    answer = []
    value = ""
    for i, v in enumerate(myStr):
        if v == "a" or v == "b" or v == "c":
            if value == "":
                continue
            answer.append(value)
            value = ""
            continue
        else:
            value += v

    if value != "":
        answer.append(value)

    return answer if answer else ["EMPTY"]
