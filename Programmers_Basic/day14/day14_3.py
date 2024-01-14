def solution(todo_list, finished):
    answer = []
    for idx, value in enumerate(finished):
        if value == False:
            answer.append(todo_list[idx])
    return answer
