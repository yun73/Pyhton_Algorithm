# N 과 M 끝내기

# 자연수 N, M
# 1 ~ N 중 M 개를 고른 수열
# 같은 수를 여러번 골라도 된다

# s : 지금까지 선택한 개수
# e : 선택할 최종 개수
# li : 지금까지 만든 리스트
def bt(s, e, li):
    # 종료조건
    if s == e:
        print(li)
        return

    # 재귀호출
    # 이전거 보다 큰 거에서 탐색
    for i in range(N):
        # 선택한 거 표시할 필요 없음
        # 그리고 다음거 고르러가자
        bt(s+1,e,li + str(i+1) + ' ')


N, M = map(int, input().split())
used = [False] * N
# li = [0] * M
# 스트링으로 하면 더 빨라?
li = ''
bt(0,M,li) # 시작, 끝
