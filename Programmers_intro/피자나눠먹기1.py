# 모든 사람이 최소 1조각은 먹어야 함
# 그럼 N명이면 N개의 조각은 있어야 하네
# 한 판에 7조각이고, N명의 사람들이 최소 1조각씩은 먹어야 한다....
# 그럼 N 나누기 7 해서 나머지는 필요없고 몫만큼의 피자 수를 구하자~


def solution(n):
    if n % 7 == 0:  # 한조각 기준으로 피자 수 와 나누어 떨어지면
        return n // 7  # n판만 시키면 됨
    else:
        return n // 7 + 1  # 아니면 애매하게 부족하니까 +1판 야호
