n = int(input())

cnt = 0
i = 0
while True:
    if n % 5 == 0:  
        cnt += n//5		
        break
    else:
        n -= 2   # 5의배수가 아니면 2씩 뺴면서 5로 나누어 떨어지도록
        cnt += 1

    if n < 0:  # 2씩 뺏을 때 음수가 되버린 경우 거슬러줄 수 없음.
        break
if n < 0:		
    print(-1)			
else:
    print(cnt)