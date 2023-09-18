# 병합정렬
from collections import deque
def merge_sort(li):
    # 종료조건 (더 이상 분할 못할 때 까지)
    if len(li) == 1:
        return li
    # 분할
    mid = len(li) // 2
    left, right = li[:mid], li[mid:] # 얕은 복사

    # 정복
    left = merge_sort(left)
    right = merge_sort(right)

    # 병합
    return merge(left,right)

def merge(left, right):
    global cnt
    left, right = deque(left),deque(right)
    result = deque() # 정렬 결과 (병합 결과)

    if left[-1] > right[-1]:
        cnt += 1
    # 인쪽과 오른쪽 둘 중에 하나라도 원소가 남아있음 진행
    while left or right:
        # 둘 다 원소가 남아있으면 누구 꺼 꺼내올건지 비교
        if left and right:
            # 왼쪽의 맨앞 원소가 오른쪽ㅇ의 맨 앞 원소보다 작으면 왼쪽 맨앞 넣기
            if left[0] <= right[0]:
                result.append(left.popleft())
            # 그게 아니면 오른쪽 맨앞 넣기
            else:
                result.append(right.popleft())
        # 왼쪽만 남아있으면
        elif left:
            result.append(left.popleft())
        # 오른쪽만 남아있으면
        elif right:
            result.append(right.popleft())

    return result


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    L = list(map(int, input().split()))
    cnt = 0
    L = merge_sort(L)

    print(f'#{tc} {L[N//2]} {cnt}')