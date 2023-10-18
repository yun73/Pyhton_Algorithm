'''
팰린드롬?

- 자연수 : N 개 1~2000
- 질문 : M 개 1 ~ 1000000
    - S와 E(1 ≤ S ≤ E ≤ N)
    - S번째 수부터 E번째 까지 수가 팰린드롬을 이루는지


- 일단 먼저
- 길이가 짝수인 경우에는
    - 해당 길이의 앞부분 절반과 뒷부분 절반이 같은지 확인해야 한다
- 길이가 홀수인 경우
    - 해당 길이의 중간 부분 상관업이 앞뒤가 같으면 된다
- S == E 인 경우 무조건 팰린드롬이다

문제의 예시를 표로 정리해보면
dp[s][e] : s 부터 e 가 팰린드롬인지 아닌지
N = 7

숫자   1 2 1 3 1 2 1
인덱   1 2 3 4 5 6 7
    1 1 0 1 0 0 0 1
    2 x 1 0 0 0 1 0
    3 x x 1 0 1 0 0
    4 x x x 1 0 0 0
    5 x x x x 1 0 1
    6 x x x x x 1 0
    7 x x x x x x 1

- S == E 인 경우를 일단 다 1로 채워준다
- V 자 모양으로 확인해주기
- 예를 들어 dp[3][3] 에서 dp[2][4] 로 가서 팰린드롬인지 확인
- dp[2][4] 는 2부터 4 까지 팰린드롬인지 확인하는건데
- 가운데 값 들이 팰린드롬이고, 2번째 4번째 숫자가 같으면 팰린드롬이다
- 가장 가운데 값을 기준으로 대칭이므로 왼쪽 아래 대각선으로
즉 s+1,e-1 방향으로 팰린드롬인지 확인해주면 된다

- 만약 해당 방향의 값이 팰린드롬이 아니면  그전 위치도 아니다
- 길이차 1,2 인 경우는 값만 같으면 팰린드롬이다
- dp 값에 이미 존재하면 그냥 반환

'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def is_palin(s,e):
    # dp 값 존재하면 반환
    if dp[s][e] != -1:
        return dp[s][e]

    if nums[s] != nums[e]:
        dp[s][e] = 0
        return dp[s][e]

    # 1칸차거나 2칸 차이면 양 끝 비교해서 같으면 1 아니면 0
    if e-s == 1 or e-s == 2:
        dp[s][e] = 1
        return dp[s][e]

    # 왼쪽 대각선 아래로 쭉 가서 하나씩 가능한지 판별
    if is_palin(s+1,e-1):
        dp[s][e] = 1
    else:
        dp[s][e] = 0

    return dp[s][e]


N = int(input())
nums = [0] + list(map(int, input().split()))
M = int(input())

dp = [[-1]*(N+1) for _ in range(N+1)]
# 자기자신 모두 1처리
for i in range(1,N+1):
    dp[i][i] = 1

# 문자 길이 2이면 두 수 같으면 팰린 드롬
for i in range(N-1):
    if nums[i]==nums[i+1]:
        dp[i][i+1]=1
        continue
    dp[i][i+1] = 0

for _ in range(M):
    s, e = map(int, input().split())
    # 만약 이미 팔별된 값이면 출력
    if dp[s][e] != -1:
        print(dp[s][e])
        continue
    is_palin(s,e)
    print(dp[s][e])
    # for line in dp:
    #     print(*line)
    # print("====")