# N 과 M 끝내기

# 자연수 N, M
# 1 ~ N 중 M 개를 고른 수열
# 같은 수를 여러번 골라도 된다
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면,
# 비내림차순이라고 한다.

# s : 지금까지 선택한 개수
# e : 선택할 최종 개수
# li : 지금까지 만든 리스트
# before : 이전 값의 인덱스
def bt(s, e, li,before):
    # 종료조건
    if s == e:
        print(li)
        return

    # 재귀호출
    # 이전거 보다 큰 거에서 탐색
    for i in range(before, N):
        # 선택한 거 표시할 필요 없음
        # 그리고 다음거 고르러가자
        bt(s+1,e,li + str(i+1) + ' ', i)


N, M = map(int, input().split())
used = [False] * N
# li = [0] * M
li = ''
bt(0,M,li,0) # 시작, 끝
