def solution(numbers):
    sum = 0
    length = len(numbers)
    for i in numbers:
        sum += i

    return sum / length
