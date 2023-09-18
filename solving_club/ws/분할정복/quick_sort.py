# 퀵 정렬
def partition(A,l,r):
    # 피봇
    p = A[l]
    # 양쪽에서 피봇 기준으로 확인할 인덱스
    i, j = l, r

    while i<=j:
        # 피봇 왼쪽에 대하여 판별
        while i<=j and A[i] <= p: # 피봇보다 작은값들이 와야 해
            i += 1
        # 피봇 오른쪽에 대하여 판별
        while i<=j and A[j] >= p:
            j -= 1

        if i < j:
            A[i], A[j] = A[j], A[i]
    # 피봇 위치 값을 좌우 작은값, 큰값으로 나워주는 기준이 되는 곳의 값과 바꿔준다
    A[l], A[j] = A[j], A[l]
    # 피봇 위치 반환
    return j


def quick_sort(A,l,r):
    if l < r:
        # 값을 구분 지어줄 기준
        s = partition(A,l,r)
        # s제외 왼쪽
        quick_sort(A,l,s-1)
        # s제외 오른쪽
        quick_sort(A,s+1,r)



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    A = list(map(int, input().split()))
    quick_sort(A,0,len(A)-1)

    print(f'#{tc} {A[N//2]}')