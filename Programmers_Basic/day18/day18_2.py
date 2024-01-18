def solution(myString):
    answer = myString.split("x")
    new = []
    for i in answer:
        if i != "":
            new.append(i)

    return sorted(new)
