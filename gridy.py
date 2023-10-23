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

- m의 합들이 M 이상이 될 때 최소 비용 기록
- 이전 앱에 최소값이 기록되어 있다면 그게 그 앱의 최소
-

'''
import sys
input = sys.stdin.readline



N, M = map(int, input().split())
m = list(map(int, input().split()))
c = list(map(int, input().split()))

# dp[i][j] :
dp = [[0]*N for _ in range(N)]


print(min(dp))