n, m = map(int, input().split())
dp = [[0]*(m+1) for i in range(n+1)]
_max = 0
for i in range(1, n+1):
    for j, board in enumerate(input(), start=1):
        dp[i][j] = int(board)
        if dp[i][j] :
            dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
            _max = max(_max, dp[i][j])
print(_max*_max)