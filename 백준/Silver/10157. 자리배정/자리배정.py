'''
IM 대비 문제 풀기
'''
# 자리배정
# 달팽이 문제
# 공연장 크기 C, R
# 1,1 부터 출발해서
# 보기 편하게 뒤집기
# 탐색방향
# 우하좌상 반복
dr = [0,1,0,-1]
dc = [1,0,-1,0]
# 아직 안채워진 방향으로 가다가 채워진 부분 나오면 다음 방향으로 ㄱㄱ
# 대기순서가 K인 관객에게 배정될 좌석번호 x,y 찾자
C, R = map(int, input().split())
K = int(input())
# 공연장 일단 만들기
# 보기 편하게 뒤집은 배열에 0열 0행 추가 -1 값 넣어주자
# 배열 추가시 리스트로 생성해서 더해줘야 하는거 조심
seat = [[-1] * (R+1)] + [[-1] + [0]*R for _ in range(C)]
# for s in seat:
#     print(s)
# 현재 위치
r,c = 1, 1
# 좌석 배정 숫자
n = 1
# 현재 위치에 좌석배정
seat[r][c] = n
# 처음에 아래 방향부터
d = 0
if K == 1:
    print(r,c)
elif K >R*C:
    print(0)
else:
    while n < R*C:
        nr = r + dr[d]
        nc = c + dc[d]
        # 만약 이동할 방향이 공연장 내부이고, 아직 방문하지 않은 좌석이면
        if 1<=nr<C+1 and 1<=nc<R+1 and seat[nr][nc] == 0:
            # 좌석 배정숫자 1 늘리고
            n += 1
            # 해당방향좌석애 좌석 배정
            seat[nr][nc] = n
            # 현재 위치를 바꿔줘
            r,c = nr, nc
            # 만약 배정숫자가 K이면 해당 자리 반환해줘
            if n == K:
                # for s in seat:
                #     print(s)
                print(nr, nc)
                break
        else:
            # 방향 전환
            d = (d+1)%4 # 0,1,2,3 반복

