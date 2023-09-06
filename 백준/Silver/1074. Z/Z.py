# Z
# 크기가 2^N * 2^N 인 2차원 배열 z모양으로 탐색
# N > 1 인경우 2^N-1 * 2^N-1 로 4등분 후 재귀적으로 순서대로 방문
'''
N = 2 일때
r : 0~2^(N-1)
c : 0~2^(N-1)
1234 사분면으로 나누기
(r,c) 가 어디 있는지 찾아야 하는 거니까
계속 나누면서 4분면 들어가다
마지막 도달 시 해당 칸이 찾는 칸
함수 인자 이용해서 몇번 째인지 구하자

한 번 나눴을 때 각 시작점들의 값이 now + 3 * 2 **(2*(N-1))
그다음 또 탐색할 때는 2^2(N-1) 만큼 차이나고

시작부분의 값을 각 사분면 시작점에 전달해주면서?

N = 1 2 3 4 5
    0 2 4 6 8
    0 1 2 3 4
'''
def sep(sr,er,sc,ec,N,now):
    global r
    global c
    global result

    mid_r = (sr + er) // 2
    mid_c = (sc + ec) // 2
    # 종료 조건
    if N < 0 and (sr,sc) == (r,c):
        result = int(now)
        return

    else: # 아직 못찾았으면 범위 확인 후 새로운 시작점 끝점 반환
        # 1사분면
        if r <= mid_r and c <= mid_c:
            # 행열 종료 값 갱신
            er, ec = mid_r, mid_c
            # 다음 작은 구역으로 넘어가기
            sep(sr, er, sc, ec, N-1, now+ 0*2**(2*(N-1)))
            # 해당 구역으로 들어가면 더이상 다른 구역 탐색 안해도 됨
            return
        # 2사분면
        elif r <= mid_r and c > mid_c:
            # 행 종료 값, 열 시작 값 갱신
            er, sc = mid_r, mid_c+1
            # 다음 작은 구역으로 넘어가기
            sep(sr, er, sc, ec, N - 1, now + 1 *2**(2*(N-1)))
            return
        # 3사분면
        elif r > mid_r and c <= mid_c:
            # 행 시작 값, 열 종료 값 갱신
            sr, ec = mid_r+1, mid_c
            # 다음 작은 구역으로 넘어가기
            sep(sr, er, sc, ec, N - 1, now + 2 * 2 **(2*(N-1)))
            return
        # 4사분면
        elif r > mid_r and c > mid_c:
            # 행열 시작 값 갱신
            sr, sc = mid_r + 1, mid_c + 1
            # 다음 작은 구역으로 넘어가기
            sep(sr, er, sc, ec, N - 1, now + 3 * 2 **(2*(N-1)))
            return

N, r, c = map(int, input().split())

# 행 인덱스
sr, er = 0, 2**(N)-1
# 열 인덱스
sc, ec = 0, 2**(N)-1

result = 0
sep(sr,er,sc,ec,N,0)

print(result)



