# 나무 자르기
# 나무 M 미터가 필요함
# 절단기 높이 H 지정
# H 보다 큰 나무는 윗 부분 잘릴거야
# 연속한 나무들 다 잘림
# 잘린 나무들을 들고 갈거
import sys

# 자를 나무 높이
# H : 자를 높이
def cut(li, H, M):
    result = 0

    for height in li:
        if height > H:
            result += height-H

    # 만약 M미터 이상의 나무를 가져갈 수 있다면
    if result >= M:
        return True
    else:
        return False

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
# 적어도 M미터의 나무를 집에 가져가기 위한 설정 높이 최대 값

# 높이값을 0 부터 max(tree) 사이에서 찾자
low = 0
high = max(tree)
# 최대값 지정
can = 0
while low <= high:
    # 자를 높이인 H = mid
    mid = (low + high)//2
    # 만약 mid에서 적어도 M미터의 나무를 가져갈 수 있다면
    if cut(tree, mid, M):
        low = mid + 1
        can = mid
    else:
        high = mid -1

print(can)



