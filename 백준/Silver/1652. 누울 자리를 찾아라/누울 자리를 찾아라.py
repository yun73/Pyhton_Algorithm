'''

방 : N x N  정사각형

누울 자리 찾기
    - 똑바로 연속해서 2칸 이상의 빈 칸이 존재하면
    그곳에 몸을 양 옆으로 쭉 뻗으면서 누울수 있다.
    가로, 세로 둘다 가능
    누울 때 무조건 몸을 쭉 뻗기 때무에 반드시 벽이나 짐에 닿게 된다

입력
방 크기 N 1 ~ 100
. 아무것도 없는 곳
X 짐 있느ㄴ곳

'''

import sys
input = sys.stdin.readline

N = int(input())

room = list(input().rstrip() for _ in range(N))

garo = 0
sero = 0


for r in range(N):
    cnt_garo = 0
    cnt_sero = 0
    for c in range(N):
        # 가로 찾는 로직
        if room[r][c] == '.':
            cnt_garo += 1
        if room[r][c] == "X" or c == N-1:
            if cnt_garo >= 2:
                garo += 1
                cnt_garo = 0
            else:
                cnt_garo = 0
        # 세로 찾는 로직
        if room[c][r] == '.':
            cnt_sero += 1
        if room[c][r] == "X" or c == N - 1:
            if cnt_sero >= 2:
                sero += 1
                cnt_sero = 0
            else:
                cnt_sero = 0

print(garo, sero)