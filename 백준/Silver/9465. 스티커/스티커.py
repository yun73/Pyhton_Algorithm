'''
스티커

- 2n개의 스티커 중에서 점수의 합이 최대가 되면서 서로 변을 공유 하지 않는 스티커 집합을 구하기
'''
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0]*(n+1) for _ in range(2)]
    dp[0][1] = sticker[0][0]
    dp[1][1] = sticker[1][0]
    start = 1
    if n>=2:
        start = 2
        dp[0][2] = sticker[1][0] + sticker[0][1]
        dp[1][2] = sticker[0][0] + sticker[1][1]

    for i in range(start+1,n+1):
        dp[0][i] = max(dp[1][i-1]+sticker[0][i-1], dp[1][i-2] + sticker[0][i-1])
        dp[1][i] = max(dp[0][i-1]+sticker[1][i-1], dp[0][i-2] + sticker[1][i-1])

    # for line in dp:
    #     print(*line)

    print(max(dp[0][n],dp[1][n]))