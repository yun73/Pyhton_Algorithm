'''
평범한 배낭

- 배낭 : 최대 K 만큼 무게
- 물건 : N개
    - 무게 : W
    - 가치 : V

- 배낭에 넣을 수 있는 물건들의 가치의 최댓값

- 물품 N 개 중 무게가 K 이하인 부분집합
- 1부터 K 까지 무게에 각각의 무게에서 최대 가치 기록
- 이렇게 하게 되면 2**N 최악 2**100 이어서 안됨

- 배낭 알고리즘, 냅색(Knapsack) 알고리즘
'''
import sys
input = sys.stdin.readline


N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1]*(K+1) for _ in range(N)]

def bt(i,now_w):

    # 지금까지의 무게의 합이 초과되면 리턴
    if now_w > K:
        # 리턴되서 가치랑 합쳐져도 불가능한 경우니까 작아야 함
        return -1e9
    # 종료조건
    if i == N:
        return 0
    # dp 값이 이미 존재 한다면
    if dp[i][now_w] != -1:
        return dp[i][now_w]

    dp[i][now_w] =max(
        bt(i+1,now_w+items[i][0])+items[i][1],
        bt(i+1,now_w)
        )

    return dp[i][now_w]

print(bt(0,0))

# ---------------------
# # 물건 , 최대 무게
# N, K = map(int, input().split())
#
# # i번째 물건의 무게 : w[i] , i번째 물건의 가치 : v[i] ,
# # dp[i][j] : i번째 물건까지 선택하는 경우에서, 최대 무게가 j인 경우
# dp = [[0]*(K+1) for _ in range(N+1)]
# # 즉 현재 i 번째 물건을 넣을 수 있다면
# # 동시에 i-1 번 물건까지 선택이 가능하고
# # i-1 번째의 최대무게인 K 에서 i번째 물건의 무게를 뺀 K-W[i]가 최대 무게일 때의 최대 가치를 더한 값이다
# # 즉 v[i] + dp[i-1][j-w[i]]
# # 만약 기본적으로 dp[i][j] = dp[i-1][j] , 이전 물건까지 가능할때 최대무게 j에서의 최대값
# # 만약 지금 최대무게보다 지금 넣을 물건이 크면 이전거를 그대로
# # 작으면 두 값중 최대 값음
# # 물건들 리스트
# w = [0]*(N+1)
# v = [0]*(N+1)
#
# for i in range(1,N+1):
#     W, V = map(int,input().split())
#     w[i] = W
#     v[i] = V
#
# for i in range(1,N+1):
#     for j in range(1,K+1):
#         if j < w[i]:
#             dp[i][j] = dp[i - 1][j]
#             continue
#         dp[i][j] = max(dp[i-1][j], v[i] + dp[i-1][j-w[i]])
#
# print(dp[N][K])