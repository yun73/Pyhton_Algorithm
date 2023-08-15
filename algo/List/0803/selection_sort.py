'''
선택 정렬
- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택해서 위치 교환하는 방식

정렬과정
- 주어진 리스트 중 최소값
- 그 값을 리스트의 맨 앞에 위치한 값과 교환
- 매처음 위치 제외 나머지 리스트 반복
'''
def selectionSort(a, N):
    for i in range(N-1):
        minidx = i
        for j in range(i+1, N):
            if a[minidx] > a[j]:
                minidx = j
        a[i], a[minidx] = a[minidx], a[i]


# k 번째 작은 수
def selectionSort(a, k):
    for i in range(0,k):
        minidx = i
        for j in range(i+1, len(a)):
            if a[minidx] > a[j]:
                minidx = j
        a[i], a[minidx] = a[minidx], a[i]
    return a[k-1]
