# N 과 M 끝내기

# 자연수 N, M
# N개의 자연수 중에서 M개를 고른 수열

# s : 지금까지 선택한 개수
# e : 선택할 최종 개수
# li : 지금까지 만든 리스트
def bt(s, e, li):
    global perm

    # 종료조건
    if s == e:
        if li not in perm:
            perm.add(li)
            print(li)
        return

    # 재귀호출
    for i in range(N):
        if not used[i]:
            # 선택한 거 표시할 필요 없음
            # 그리고 다음거 고르러가자
            used[i] = True
            bt(s+1,e,li + str(nums[i]) + ' ')
            used[i] = False

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
used = [False] * N
perm = set()
li = ''
bt(0,M,li) # 시작, 끝
