def best(r, N, music):
    global min_cnt
    global choose
    global can_play

    # 끝까지 도달하고 뮤직을 다 연주할 수 있으면
    if r == N :
        cnt = 0  # 사용하는 기타의 개수 세기
        for m in range(M):
            if music[m] > 0:
                cnt += 1
        if cnt == can_play:
            g_cnt = 0
            for gui in choose:
                if gui == 1:
                    g_cnt += 1
            if min_cnt > g_cnt:
                min_cnt = g_cnt

    else:
        if choose[r] == 0:
            choose[r] = 1
            # 각 기타의 연주가능 노래 스트링 돌면서
            # 연주가능한 곡 체크
            for i in range(M):
                if all[r][1][i] == 'Y':
                    music[i] += 1
            best(r+1, N, music)
            choose[r] = 0
            # 연주가능한 곡 초기화
            for i in range(M):
                if all[r][1][i] == 'Y':
                    music[i] -= 1
            best(r+1, N, music)

# N : 기타의 개수, M : 곡의 개수
N, M = map(int, input().split())
all = [0] * N
for n in range(N):
    guitar, play = input().split()
    all[n] = [guitar, play]
# print(all)
# 기타를 살지 말지 정할 리스트
choose = [0] * N
# 연주할 수 있는 음악 체크
music = [0] * M
# 사용하는 기타의 최소 개수
min_cnt = 11
can_music = [0] * M
# 최대로 연주할 수 있는곡
can_play = M
for g in range(N):
    for i in range(M):
        if all[g][1][i] == 'Y':
            can_music[i] += 1
for i in range(M):
    if can_music[i] == 0:
        can_play -= 1

best(0, N, music)
if can_play == 0:
    min_cnt = -1

if min_cnt == 11:
    min_cnt = -1

print(min_cnt)