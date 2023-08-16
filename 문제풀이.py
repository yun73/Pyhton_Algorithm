# 백준, 프로그래머스 문제풀이용
# 오목
# 탐색방향
# 오,왼,오아대,왼위대,아래,위, 왼아대,오위대
dr = [0, 0, 1, -1, 1, -1, 1, -1]
dc = [1, -1, 1, -1, 0, 0, -1, 1]


# 검돌 1, 흰돌 2, 나머지 0
# 검승 1, 흰승 2, 승부결정 아직 0
# 이긴 바둑알 중 좌상 에 위치한 좌표 출력
def omok(r, c, color):
    # 4방향 탐색
    for d in range(4):
        cnt = 1
        for i in range(2):
            # 5보다 많으면 이긴거 아니므로
            # 반대방향 짝지어서 개수 세기
            # 근데 만약 이긴다면 결국 현재위치가 우승점이 될거임
            ld = 2 * d + i  # local_d
            nr = r + dr[ld]
            nc = c + dc[ld]
            while 0 <= nr < 19 and 0 <= nc < 19 and board[nr][nc] == color:
                print(nr, nc)
                cnt += 1
                nr += dr[ld]
                nc += dc[ld]
        if cnt == 5:
            print(color)
            print(f'{r + 1} {c + 1}')
            return 1
    else:
        return 0


board = [list(map(int, input().split())) for _ in range(19)]

# 바둑알이 흰색이거나 검정색이면 판정 함수 실행
# 시작위치
result = 0  # 승부결과
# while result < 1 and r < 19:
for r in range(19):
    if result == 1:
        break
    for c in range(19):
        if board[r][c] == 1 or board[r][c] == 2:
            result = omok(r, c, board[r][c])
            if result == 1:
                break
else:
    print(0)

    # else:
    #     c += 1
    #     if c == 19:
    #         r += 1
    #         c = 0

if result == 0:
    print(0)
