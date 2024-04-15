def solution(seoul):
    for index, value in enumerate(seoul):
        if value == 'Kim':
            return f"김서방은 {index}에 있다"