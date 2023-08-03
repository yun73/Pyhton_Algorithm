# NxN 크기의 단어퍼즐
# 특정길이 K 인 단어 들어갈 수 있는 자리의 수를 출력

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    # N 은 퍼즐의 가로세로 길이, K는 단어길이
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    # 0 = 검은색, 1 = 흰색
    # 흰색에 단어 넣는거 가능, 딱 맞게 들어가야함

    # 행별로 가능한 자리 찾아보기
    # 앞에서 부터 차례대로 하며
    count = 0
    for r in range(N):
        r_k = [0] * (N + 2)  # 행별 연속된 자리수 기록
        c_k = [0] * (N + 2)  # 열별 연속된 자리수 기록
        for c in range(N):
            if puzzle[r][c] == 1:
                r_k[c + 1] = 1
            if puzzle[c][r] == 1:
                c_k[c + 1] = 1

        for p in range(N+1):
            if r_k[p] == K:
                if r_k[p+1] < r_k[p]:
                    count += 1
            if c_k[p] == K:
                if c_k[p + 1] < c_k[p]:
                    count += 1
    # 만약 길이가 K라면

    print(f'#{tc} {count}')
