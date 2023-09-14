# 상어 초등학교
'''
한 칸에는 학생 한 명의 자리만 있을 수 있고
|r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸이 (r1, c1)과 (r2, c2)를 인접
-> 상하좌우만 탐색하면 돼
'''
'''
앉은 자리는 체크해줘야 함 - visited or seat 자리 배치 그냥 사용?
1 .우선 빈 칸 중 좋아하는 학생이 인접한 칸에 가장 많은 칸
2 . 1 만족하는 칸들을 저장한 리스트 -> 인접한 칸 중 빙어있는 칸 많은 칸으로 
- 그러면 1의 리스트에 인접 빈칸 개수 같이
3. 2를 만족하는 칸을 저장한 리스트도 -> 이중 행 열 번호가 가장 작은칸 - 정렬해서 맨 앞에거
'''
def find_like(like_stu):
    max_like = -1
    like_list = []
    max_v = -1
    for r in range(N):
        for c in range(N):
            # 해당자리에 안앉아있어야지 가능
            if not seat[r][c]:
                # 인접 방향에 좋아하는 학생이 있는지 세주고
                cnt_like = 0
                cnt_v = 0
                for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                    nr, nc = r + dr, c + dc
                    # 탐색 범위가 반 크기 이내이고
                    if 0<=nr<N and 0<=nc<N:
                        # 거기에 있는 얘가 내가 좋아하는 얘이면
                        if seat[nr][nc] in like_stu:
                            cnt_like += 1
                        elif not seat[nr][nc]: # 빈자리이면
                            cnt_v += 1

                # 다 돌고 나와서
                if max_like < cnt_like: # 좋아하는얘 많은 공간 찾으면
                    # 새로운 리스트 만드거니까 초기화
                    max_v = -1
                    if max_v < cnt_v:
                        max_v = cnt_v
                    # max_like를 갱신하고
                    max_like = cnt_like
                    # like_list 를 초기화하고
                    like_list = []
                    # like_list 에 현재 위치랑 빈칸 개수 넣어줘
                    like_list.append((r,c,cnt_v))
                elif max_like == cnt_like: # 만약 같은 조건인 얘 찾으면
                    if max_v < cnt_v:
                        max_v = cnt_v
                    like_list.append((r, c, cnt_v))
                # 이하인 얘는 그냥 버리자
    # 다 돌고나면 like_list를 반환해줘
    return like_list, max_v



N = int(input())

# 자리배열
seat = [[0]*N for _ in range(N)]

# 학생 번호가 인덱스인 리스트
like = [0] *(N*N+1)
perm = []
# 번호와 좋아하는 사람 입력 받기
for _ in range(N*N):
    stu, *like_stu = map(int, input().split())
    # 학생 stu 위치에 좋아하는 학생 리스트 넣어
    like[stu] = like_stu
    perm.append(stu)


for i in perm:
    # 1 .우선 빈 칸 중 좋아하는 학생이 인접한 칸에 가장 많은 칸
    # 인접한 칸 세어주면서 max_like 를 세어주자
    like_list, max_cnt = find_like(like[i]) # i의 자리를 ㅑ가 좋아하는 학생 목록을 가져가서 찾아줘

    # 2 . 1 만족하는 칸들을 저장한 리스트 -> 인접한 칸 중 빙어있는 칸 많은 칸으로
    # - 그러면 1의 리스트에 인접 빈칸 개수 같이
    # 빈칸 조건 만족하는 리스트
    v_list = []
    # print(like_list)
    # print(max_cnt)
    for info in like_list: # 하나씩 꺼내서 보자
        if info[2] == max_cnt: # 만약 빈칸 개수 최대이면
            v_list.append((info[0],info[1])) # 좌표값만 넣어줘
    # print(v_list)
    # v_list 를 정렬해서 좌측 상단의 값을 자리로 하자
    v_list.sort()
    # print(v_list)
    # 조건 맞는 자리에 앉았다고 표시  3. 2에서 넘ㅇ온 리스트고 갑 ㅅ여러개면 젤 작은 자리에
    seat[v_list[0][0]][v_list[0][1]] = i

result = 0
# 다 넣었으면 만족도 조사해주자
for r in range(N):
    for c in range(N):
        # 현재 위치 학생 = seat[r][c]
        cnt = 0
        for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
            nr = r + dr
            nc = c + dc
            # 인접 위치 학생 seat[nr][nc]
            if 0 <= nr < N and 0 <= nc < N and (seat[nr][nc] in like[seat[r][c]]):
                cnt += 1
        if cnt > 0:
            result += 10**(cnt-1)

print(result)



