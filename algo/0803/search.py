# 저장된 자료중 원하는 항목 찾기
# 탐색 키를 가진 항목 찾기
# 검색 종류 : 순차검색, 이진 검색, 해시
# 이진 검색 중요

# 순차검색
# 일렬로 되어있는 자료 순서대로 검색
# 1. 정렬되어 있지 않은 경우, 2. 정렬된 경우 에 대해서

# 이진 검색
# 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행
# 목적 키를 찾을 때 까지 이진 검색을 순환적으로 반복 수행
# 이진 검색을 위해서 자료가 정렬되어 있어야 함
# 구현
def binary_search(a, N, key):
    start = 0
    end = N-1
    while start <= end : # 탐색구간이 존재, 원소 한개 이상이면 탐색하야함
        middle = (start + end)//2
        if a[middle] == key : # 검색성공
            return True
        elif a[middle] > key :
            end = middle -1
        else:
            start = middle +1

    return False
