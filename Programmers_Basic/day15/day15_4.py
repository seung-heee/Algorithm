def solution(num_list):
    answer = 0
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        return eval("*".join(map(str, num_list)))
    return answer
