# N 과 M 끝내기

# 자연수 N, M
# 1 ~ N 중 중복 없이 M 개를 고른 수열

# s : 지금까지 선택한 개수
# e : 선택할 최종 개수
# perm : 출력할 숫자 모음
def bt(s, e, perm):
    # 종료조건
    if s == e:
        print(*perm)
        return

    # 재귀호출
    for i in range(N):
        if not used[i]:
            # 선택했다고 체크하고
            used[i] = True
            # 그리고 다음거 고르러가자
            # 출력할 거 넘겨줘
            perm[s] = i+1
            bt(s+1,e,perm)
            # 갔다와서 초기화하고 다른 경우로 가자
            perm[s] = 0
            used[i] = False


N, M = map(int, input().split())
used = [False] * N
# 나타낼 수열
perm = [0]*M
bt(0,M,perm) # 시작, 끝
