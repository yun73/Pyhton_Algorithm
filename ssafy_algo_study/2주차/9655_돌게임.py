n = int(input())
# N개에서 마지막 3개 or 1개 가져가면 이기는거
# 1개 가져가는 거랑 3개 가져가는 거랑 같나?
dp = [0]*1001
dp[1] = 1 # SK 승리
dp[2] = 0 # CY 승리
dp[3] = 1 # SK 승리

for i in range(4, n + 1):
    if dp[i - 1] == 1 or dp[i - 3] == 1:
        dp[i] = 0

    else:
        dp[i] = 1

if dp[n] == 1:
    print("SK")

else:
    print("CY")


