'''
계단 오르기

- 계단 아래서 꼭대기 까지
- 계단 :
    - 각 계단마다 점수 존재
- 올라가기
    - 한 번에 한 계단씩 or 두 계단씩
    - 연속된 세 개의 계단을 모두 밟으면 안됨
    - 시작점은 계단에 포함 X
    - 도착 계단은 반드시 밟아야 한다.

- 각 층까지의 최대 점수를 저장
- 현재층까지 오는 경우는 2칸 전이나 1칸전
- 근데 이전 계단에서 1칸이미 올라온 상태인데 거기서 2칸이면 3칸이 되니까

'''

# 계단의 개수
N = int(input())
score = [0]+[int(input()) for _ in range(N)]
# print(score)

# dp[i][0] 한칸으로 올라오는 경우의 최대값
dp = [[0,0] for _ in range(N+1)]
# 그럼 다음거에서 가능한 경우는
# 2번쨰 전거의 1,2 중 최대 + 자기거
# max(dp[i-2][0],dp[i-2][1]) + score[i] 
# 1번째 전거의 2 + 자기거
# dp[i-1][1] + score[i]
if len(score)<=3: # 계단이 2개 이하
    print(sum(score))
else: # 계단이 3개 이상일 때
    dp[1][0]= score[1] 
    dp[1][1] = score[1]
    dp[2][0]=score[2]+score[1] 
    dp[2][1]=score[2]
    for i in range(3,N+1): # 3번째 계단 부터 dp 점화식 이용해서 최대값 구하기
        dp[i][0] = dp[i-1][1] + score[i]
        dp[i][1] = max(dp[i-2][0],dp[i-2][1]) + score[i] 
        # print(dp)
    print(max(dp[N][0],dp[N][1]))

# dp = [0]*(N+1)
# # 시작점은 첫번째 계단으로 한칸으로든 두칸으로든 계단 오른 횟수에 영향 안줌
# # 끝점은 무조건 밟아야 하니까 거꾸로 돌자
# if len(score)<=3: # 계단이 2개 이하
#     print(sum(score))
# else: # 계단이 3개 이상일v 때
#     dp[N]=score[N] # 마지막 계단 초기설정
#     dp[N-1]=score[N]+score[N-1] # 마지막 두번쨰 계단 계산
#     dp[N-2] = score[N] + score[N-2]
#     for i in range(N-3,-1,-1): # 3번째 계단 부터 dp 점화식 이용해서 최대값 구하기
#         dp[i]=max(dp[i+3]+score[i+1]+score[i], dp[i+2]+score[i])
#         # print(dp)
#     print(max(dp[0],dp[1]))