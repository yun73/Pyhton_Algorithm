# N 과 M 끝내기

# 자연수 N, M
# 1 ~ N 중 길이가 M인 수열
# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.

# s : 지금까지 선택한 개수
# e : 선택할 최종 개수
# li : 지금까지 만든 리스트
def bt(s, e, li):
    # 종료조건
    if s == e:
        print(li)
        return

    # 재귀호출
    for i in range(N):
        # 선택한 거 표시할 필요 없음
        # 그리고 다음거 고르러가자
        bt(s+1,e,li + str(nums[i]) + ' ')


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
li = ''
bt(0,M,li) # 시작, 끝
