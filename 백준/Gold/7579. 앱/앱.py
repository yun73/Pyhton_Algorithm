'''
앱

- 앱 :
    - 실행중 : 한 개, 화면에 보임
    - 활성화 : 여러개, 화면에 보이지 않아도 메인 메모리에 직전의 상태 기록

    - 비활성화 : 메모리 부족상태에서 새로운 앱 실행 시키기 위해 활성화 앱들 중 몇 개 선택하여 메모리로부터 삭제

- 앱 : N 개 , A1~AN
    - 각각 mi 바이트 만큼 메모리 사용
    - 비활성 화 후 다시 실행시 추가 비용 ci

- 새로운 앱 B 실행 : M 바이트 메모리 필요
- 활성화 상태인 A 중 몇개 비활성화 >> M 바이트 이상의 메모리 추가확보
- ci의 합 최소

- m의 합들이 M 이상이 될 때 최소 비용 기록 X
- cost에 따라 해당 cost 일 때 최대 메모리를 구하기
- 냅색 알고리즘

'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

# dp[i][j] => 1~i번째 앱까지, j의 cost로 확보 가능한 메모리의 최대
dp = [[0 for _ in range(sum(cost) + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(0, sum(cost) + 1):
        if j >= cost[i - 1]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i - 1]] + memory[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]

for i, Memory in enumerate(dp[N]):
    if Memory >= M:
        print(i)
        break
