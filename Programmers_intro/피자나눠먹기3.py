# 피자를 2~10조각까지 원하는 만큼 잘라줌
# 조각 수 slice / 먹는 사람 n명
# n명이 최소 한 조각 이상 먹으려면 최소 몇 판???
# n명 // slice >> 몫(피자 판 수)


# 피자나눠먹기1을 응용해서 조건문을 나누지 않고
def solution(slice, n):
    return (n - 1) // slice + 1  # 임의로 사람 1명 줄이고 1판 더 시키기 작전
