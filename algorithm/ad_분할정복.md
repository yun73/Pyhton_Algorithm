# 분할정복

## 문제 : 가짜 동전 찾기
- n 개의 동전들 중에 가짜 동전이 하나 포함 되어 있는데 양팔 저울을 이용해서 찾아내자
- 진짜 동전 무게 동일, 가짜 동전 조금 가볍다
- 최소로 사용 -> 12개 12개로 나누어 가벼운쪽을 다시 조사

## 분할정복 기법
- 설계 전략
    - 분할(Divide) : 해결할 문제를 여러개의 작은 부분으로 나눈다 = 나눌 수 없을 때 까지  == 문제를 쉽게 해결할 수 있을 때 까지
    - 정복(Conquer) : 나눈 작은 문제를 각각 해결한다
    - 통합(Combine) : (필요하다면) 해결된 해답을 모은다

### 거듭 제곱의 분할 정복 알고리즘

---------------

### 병합 정렬(Merge Sort)
- 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
- 분할 정복 알고리즘 활용
    - 자료를 최소 단위의 문제까지 나누구 차례대로 정렬하여 최종 결과
    - top down
- 시간 복잡도 = O(NlogN) > 최악 최선 모두 보장
- 분할 = 하나로만 남을 때 까지 분리
- 정복 = 정렬 하면서 합침

- 구조가 변하지 않는다 -> 재귀
```py
def merge_sort(m): # m = list_m
    # 종료조건 (더 이상 분할 못할 때 까지)
    if len(m) == 1:
        return m
    # 분할
    mid = len(m) // 2
    # left, right = m[:mid], m[mid:] # 얕은 복사
    left = []
    right = []

    for i in range(mid+1):
        left.append(m[i])
    for i in range(mid+1,len(m)+1):
        right.append(m[i])

    # 정복
    left = merge_sort(left)
    right = merge_sort(right)

    # 병합
    return merge(left,right)
```

```py
def merge(left, right):
    result = [] # 정렬 결과 (병합 결과)

    # i, j :
    # i => 왼쪽 리스트에서 원소를 꺼낼 위치
    # j => 오른쪽 리스트에서 원소를 꺼낼 위치

    # 인쪽과 오른쪽 둘 중에 하나라도 원소가 남아있음ㄴ 진행
    while left or right:
        # 둘 다 원소가 남아있으면 누구꺼를 꺼내올건지 비교
        if left and right:
            # 왼쪽의 맨앞 원소가 오른쪽ㅇ의 맨 앞 원소보다 작으면 왼쪽 맨앞 넣기
            if left[0] <= right[0]:
                result.append(left.pop(0))
            # 그게 아니면 오른쪽 맨앞 넣기
            else:
                result.append(right.pop(0))
        # 왼쪽만 남아있으면
        elif left:
            result.append(left.pop(0))
        # 오른쪽만 남아있으면
        elif right:
            result.append(right.pop(0))

    return result
```

### 퀵정렬(Quick Sort)

- 병합 정렬과 다른점
    1. 병합 정렬은 그냥 두부분으로 나누지만, 퀵정렬은 분할시 기준 아이템(pivot item)을 중심으로, 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킨다.
    2. 각 부분 정렬ㅇ 끝난후, 병합 정렬은 병합이란 후처리 작업 필요하지만 퀵정렬은 필요 없음

- 호어 파티션
- 로무토 파티션

- Hoare vs Lomuto
    - lomuto 는 같은 숫자가 많으면 필요없는 정렬이 많이 일어남

```py
# Hoare partition 알고리즘

# A : 정렬할 대상 리스트
# l : 왼쪽 인덱스
# r : 오른쪽 인덱스

def quick_sort(A,l,r):
    if l < r:
        # 분할하고 피봇의 위치를 구한다.
        s = partition(A, l, r)
        # s의 위치는 정해지고 s의 나머지 부분에 대해서 분할정렬 이어가기
        # s를 제외한 왼쪽 부분 정렬
        quickSort(A,l,s-1)
        # s를 제외한 오른쪽 부분 정렬
        quickSort(A,s+1,r)

```
```py
def partition(A,l,r)
    # 피봇 정하기(제일 왼쪽 부분)
    p = A[l]

    # 피봇보다 작은거는 왼쪽부터 놓고, 큰거는 오른쪽부터 놓고
    i, j = l, r
    # i : 왼쪽에 있으면 안되는 원소의 위치를 찾는 인덱스
    # 피봇보다 큰 원소의 위치 왼쪽부터 찾기

    # j : 오른쪽에 있으면 안되는 원소의 위치를 찾는 인덱스
    # 피봇보다 작은 원소의 위치를 오른쪽 부터 찾기

    while i<=j:
        # 피봇보다 큰거를 왼쪽부터 찾기 시작
        while i<=j and A[i] <= p:
            # i 번 쨰 위치에 있는 원소가 피봇보다 작으면 오른쪽으로 한칸 가서
            # 찾기 계속
            i += 1
        # 피봇보다 작은 거를 오른쪽에서 찾기 시작
        while i <= j and A[j] >= p:
            # i 번 쨰 위치에 있는 원소가 피봇보다 작으면 오른쪽으로 한칸 가서
            # 찾기 계속
            j -= 1
        # i가 j 보다 작으면 위치가 잘못된 두 원소를 찾음
        if i<j:
            # 잘못된 원소끼리 자리 교환
            A[i],A[j] = A[j], A[i]

    # 반복이 끝나면 작은것과 큰것이 다 제자리에 있다,
    # 피봇의 위치를 정해준다.
    A[l], A[j] = A[j] , A[l]

    # 정렬이 끝난 피봇의 위치를 return
    return j
```



-----------

## **이진 검색** - 코테 단골문제
- 원하는 데이터를 빨리 찾자
- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검생을 진행
- 검색범위를 반으로 줄여감
- 이진 검색을 위해서 자료가 정렬된 상태여야 함


### 문제 : 병뚜껑 속의 숫자 게임
- 숫자를 말하고 접답 숫자가 up,down 인지 알려주고 계속해서 맞춰 나가는것
- 남은 숫자 범위의 가운데 값을 부르는 것이 가장 빠른 방법

- 검색과정
    1. 자료의 중앙에 있는 원소 고른다
    2. 중앙 원소의 값과 찾고자 하는 목표값을 비교
    3.  목표갑싱 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로검생수행, 크담ㄴ 자료의 오른쪽 반에 대해서 새로 검색 수행
    4. 찾고자 하는 값을 찾을 때 까지 1~3 과정 반복

```py
# 이진 검색 - 반복문
arr = [2,4,7,9,11,19,23]

# 문제에서 데이텉가 정렬되어 있다 라는 조건이 없다면
# 반드시 정렬을 먼저 수행해야한다.
arr.sort()

def binarySearch(target):
    low = 0
    high = len(arr) - 1

    # low > high 라면 데이터를 못찾은 경우
    while low <= high:
        mid = (low + high) // 2

        # 1. 가운데 값이 정답인 경우
        if arr[mid] == target:
            return mid
        # 2. 가운데 값이 정답보다 작은경우
        elif arr[mid] < target:
            low = mid + 1
        # 3. 가운데 값이 정답보다 큰 경우
        else:
            high = mid - 1

    return "해당 데이터는 없습니다."
```

```py
# 이진 검색 - 재귀호출 활용
arr = [2,4,7,9,11,19,23]

# 문제에서 데이텉가 정렬되어 있다 라는 조건이 없다면
# 반드시 정렬을 먼저 수행해야한다.
arr.sort()

# 함수 한 번 호출 때 마다 low, high 변수가 바뀌어서 사용딤
def binarySearch(low,high,target):
    # 기저 조건 : 언제까지 재귀호출을 반복할 것인가?
    # low > high 라면 데이터를 못 찾음
    if low > high:
        return -1

    mid = (low + high) // 2

    # 1. 가운데 값이 정답인 경우
    if target == arr[mid]:
        return mid
    # 2. 가운데 값이 정답보다 작은경우
    elif arr[mid] < target:
        return binarySearch(mid+1,high,target)
    # 3. 가운데 값이 정답보다 큰 경우
    else:
        return binarySearch(low, mid - 1, target)

print(f'9 = {binarySearch(0,len(arr)-1,9)}')
```

------------

sort(), sorted()
내장 라이브러리가 굉장히 강력!

- 병합 정렬
    - 직접 구현할 일은 적다
        - -> 멀티 쓰레드
    - 과거에 면접 단골 질문 + 분할 정복 학습에 좋다
        - -> 코드를 보기 전에 반드시 손으로 직접 해보기

- 퀵 정렬
    - 직접 구현할 일은 적다
        - 평균적으로 굉장히 좋음 O(NlogN)
        - 특히, 큰 데이터를 다룰 때 좋다.
        - 단점 : 역순 정렬 등 최악의 경우 O(N^2)
    - 과거에 면접 단골 질문 + 분할 정복 학습에 좋다
        - -> 코드를 보기 전에 반드시 손으로 직접 해보기

- 이진검색
    - 코딩 테스트의 메인 알고리즘 중 하나
    - 목적 : "원하는 값을 빨리 찾는 것"
    - 시간 : O(logN)
    - Parametric Search
        - lower bound
        - upper bound
            - 여러개의 데이터 중 2가 처음 나온 시점
            - 2~9 사이의 데이터는 몇개인가?
--------
