def solution(num_list):    
    answer = [idx for idx, value in enumerate(num_list) if value < 0]
    return answer[0] if answer else -1
