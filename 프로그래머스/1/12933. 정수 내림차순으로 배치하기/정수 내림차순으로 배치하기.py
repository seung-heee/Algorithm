def solution(n):
    digits = [int(digit) for digit in str(n)]

    sorted_digits = sorted(digits, reverse=True)

    sorted_number = int(''.join(map(str, sorted_digits)))
    
    return sorted_number