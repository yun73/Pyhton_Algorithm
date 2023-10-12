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

# def bt(i,N,K,now_w,sum_v):
#     global dp
#     global arr
#
#     # 지금까지의 무게의 합이 초과되면 리턴
#     if now_w > K:
#         return
#     # 무게 합이 초과가 아니라면 지금까지의 무게합일 때의 가치를 갱신
#     # 가치 합이 저장된 거 보다 작으면 탐색 안해도 돼
#     # K보다 작을 때 같은 경우여도 뒤에 더 커지게 할 수도 있음
#     dp[now_w] = max(dp[now_w],sum_v)
#
#     # 종료조건
#     if i == N:
#         return
#     if now_w == K:
#         return
#     # i 번째 물건을 넣을지 말지 결정하면서 진행
#     bt(i+1,N,K,now_w+arr[i][0],sum_v+arr[i][1])
#     # 배낭에 안넣고 가기
#     bt(i+1,N,K,now_w,sum_v)


# 물건 , 최대 무게
N, K = map(int, input().split())

# i번째 물건의 무게 : w[i] , i번째 물건의 가치 : v[i] ,
# dp[i][j] : i번째 물건까지 선택하는 경우에서, 최대 무게가 j인 경우
dp = [[0]*(K+1) for _ in range(N+1)]
# 즉 현재 i 번째 물건을 넣을 수 있다면
# 동시에 i-1 번 물건까지 선택이 가능하고
# i-1 번째의 최대무게인 K 에서 i번째 물건의 무게를 뺀 K-W[i]가 최대 무게일 때의 최대 가치를 더한 값이다
# 즉 v[i] + dp[i-1][j-w[i]]
# 만약 기본적으로 dp[i][j] = dp[i-1][j] , 이전 물건까지 가능할때 최대무게 j에서의 최대값
# 만약 지금 최대무게보다 지금 넣을 물건이 크면 이전거를 그대로
# 작으면 두 값중 최대 값음
# 물건들 리스트
w = [0]*(N+1)
v = [0]*(N+1)

for i in range(1,N+1):
    W, V = map(int,input().split())
    w[i] = W
    v[i] = V

for i in range(1,N+1):
    for j in range(1,K+1):
        if j < w[i]:
            dp[i][j] = dp[i - 1][j]
            continue     
        dp[i][j] = max(dp[i-1][j], v[i] + dp[i-1][j-w[i]])
   
print(dp[N][K])