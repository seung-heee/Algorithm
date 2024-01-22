def solution(rank, attendance):
    answer = 0
    res = [rank[idx] for idx, value in enumerate(attendance) if value == True]
    res = sorted(res)[:3]
    answer = rank.index(res[0]) * 10000 + rank.index(res[1]) * 100 + rank.index(res[2])
    return answer
