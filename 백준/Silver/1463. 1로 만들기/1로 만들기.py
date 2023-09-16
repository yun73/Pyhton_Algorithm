# 1로 만들기
'''
1. 사용 횟수의 최솟값이므로 1,2 순으로 적용되고
2. 1을 빼는 것은 3이나 2로 나워질 수 있게 하는 용도이다
11 10 5 4 2 1
11 10 9 3 1
3. 
일단 모든 수는 2n 과 2n+1로 나타낼 수있다  
2n+1 이 3의 배수 일때는 3으로 나눈 값의 최소 횟수에 1을 더해준다
2n+1 이 3의 배수가 아닐때는 -1 연산을 한 값의 최소값에 1을 더한다
2n 은 무조건 2의 배수인다 -1한게 3의 배수이면 그걸 따라간다
근데 1을 빼고 2로 나눴을떄 최소가 되는 경우도 존재한다
그럼 위의 3개지 값중에 최소값을 따라가야한다
 '''
# dp[N] = 최소 연산횟수
dp = [0]*(10**6+1)
# 1 일 때 연산횟수 0
dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 2  # 4-1 1 + dp[3]
dp[5] = 3 # 5-1 1 + dp[4]
dp[6] = 2 # 6/3 1 +dp[2]
N = int(input())
for i in range(7,N+1):
    # 2와 3의 배수가 아닐때
    dp[i] = dp[i-1] + 1
    # 3의 배수일 때
    if not i%3:
        dp[i] = min(dp[i//3]+1,dp[i])
    # 2의 배수일 때
    if not i%2:
        dp[i] = min(dp[i//2] + 1, dp[i])

print(dp[N])