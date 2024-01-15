def solution(arr):
    answer = 0

    while True:
        temp = arr.copy()  # 기존 배열을 복사하여 temp에 저장

        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] //= 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = (arr[i] * 2) + 1

        if arr == temp:  # 변형 전과 후의 배열이 같으면 반복 종료
            break

        answer += 1  # 반복 횟수 증가

    return answer
