import sys
input = sys.stdin.readline

N = int(input())
Xarr = list(map(int, input().rstrip().split()))

zipArr = sorted(set(Xarr))

dict_idx = {}
# for i in range(N):
#   # 각 원소에 대해 압축된 인덱스를 딕셔너리에 저장
#   dict_idx[Xarr[i]] = zipArr.index(Xarr[i])

# 압축된 인덱스를 저장할 딕셔너리 생성
dict_idx = {zipArr[i]: i for i in range(len(zipArr))}

print(' '.join([str(dict_idx[i]) for i in Xarr]))