# N*N 크기의 도시에 홈방범 서비스
# 마름모 영역만 서비스 제공
# 운영비용 = 서비스 영역의 면적 = K * K + (K - 1) * (K - 1)
# 제공받는 집들 각각 M 의 비용 지불
# 보험회사 손해 보지 않는 한 최대한 많은 집
# 도시의 크기 N, 집 지불 M

# 손해를 보지 않고 홈방범 서비스를 가장 많은 집들에 제공하는 서비스 영역 찾기

# 그 때의 홈방범 서비스를 제공 받는 집들의 수를 출력
# 보안회사의 이익(4) = 서비스 제공받는 집들을 통해 얻는 수익(3*3) - 운영 비용(5)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    # 가장 많은 집에 제공
    many_home = 0
    # 행과 열을 순회하며 각 위치마다 k를 늘려가며 탐색
    for r in range(N):
        for c in range(N):
            # k은 1일 때부터 마름모 모양으로 탐색 시작
            # 정사각형 2k-1 부분에서 i-j 의 값 즉 중심으로부터 거리가 k-1 인데 탐색
            for K in range(1, N + 2):
                # 지금 영역에서의 집의 개수
                home = 0
                # -k+1부터 +k-1 까지
                for i in range(r-K+1, r+K):
                    for j in range(c-K+1,c+K):
                        if 0<=i<N and 0<=j<N and abs(i - r) + abs(j - c) <= K-1 and city[i][j] == 1:
                            home += 1
                # 나가는 돈
                money = K * K + (K - 1) * (K - 1)
                # 들어노는 돈
                profit = home * M
                if profit >= money:
                    if many_home < home:
                        many_home = home

    print(f'#{tc} {many_home}')