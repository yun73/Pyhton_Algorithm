# 공통점 : 주어진 리스트를 두 개로 분할하고, 각각을 정렬
# 합병정렬 : 단순하게 두 부분으로 나눔, 정렬 끝난후 합병이란 후처리 작업 필요
# 퀵정렬 : 분할시 기준아이템 피봇을 중심으로 작왼, 큰오 로 위치, 각 부분 정렬 끝나고
# 후처리 작업 없음
# 퀵 정렬 알고리즘
def quickSort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end) # 주어지는 배열, 시작 , 끝으로 나눌 부분
        quickSort(a,begin, p-1) # 피봇 기준 왼쪽
        quickSort(a,p+1, end) # 피봇 기준 오른쪽

# partition 구하는 함수
def partition(a, begin, end): # 주어지는 배열의 피봇 구하기
    pivot = (begin + end)//2
    L = begin
    R = end
    while L < R: # 왼쪽 오른쪽에서 피봇 방향으로 움직이며
        # 피복보다 작은 값은 왼쪽으로 이동시킴, 큰값은 오른쪽
        while(a[L] < a[pivot] and L<R):
            L +=1
        while(a[R] >= a[pivot] and L<R):
            R -=1
        if L < R :
            if L == pivot:
                pivot = R
            a[L], a[R] = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
    return R
