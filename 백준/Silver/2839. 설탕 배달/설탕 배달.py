# 설탕 배달
# 봉지 3키로, 5키로
dp = [-1] * 5001
dp[3] = 1
dp[5] = 1
# dp[6] = 2
# dp[8] = 2
# dp[9] = 3
# dp[10] = 2
# dp[11] = 3
# 봉지 가장 적게 해야하므로
# 5키로 짜리만 더해서 들 수 있는지 검사
# 그다음 3키로
# 근데 지금 해당하는 값에 3과 5를 빼도 안되면 -1
for n in range(6,5001):
    if dp[n-5] != -1:
        dp[n] = dp[n-5] + 1
    elif dp[n-3] != -1:
        dp[n] = dp[n - 3] + 1
    else:
        dp[n] = -1

N = int(input())
print(dp[N])

## 다른 풀이
n = int(input()) # 설탕

result = 0 # 봉지 수

while n >= 0:
    if n % 5 == 0: # 5로 나눈 나머지가 0인 경우
        result += n // 5 # 5로 나눈 몫 추력
        print(result)
        break
    n -= 3 # 설탕이 5의 배수가 될때까지 반복
    result += 1 # 봉지 추가
else:
    print(-1) # while문이 거짓이 되면 -1 출력
