# 선택정렬 재귀
# selection_Sort(i):# i 번째 자리에 놓을 리스트에서 i 번째로 작은 원소 찾기
# 리스트 길이 5라면
# selection_Sort(0):# 0 번째 자리에 제일 작은 원소 놓기
# selection_Sort(1):# 0 번째 자리에 그 다음 작은 원소 놓기

def selection_Sort(i, N, arr):
    # 종료조건
    # N-1 번째 까지만 정렬해주면 마지막 자리는 자동으로 정렬됨
    if i == N-1:
        return

    # i번 인덱스에서 해야할 일
    else:
        # 제일 작은 값을 가진 인덱스
        # 앞에서 부터 차례대로 채워 나가므로 i로 설정하고
        minI = i
        # 배열의 i 번째 다음 요소들 부터 탐색하여
        for j in range(i + 1, N):
            # 제일 작은값 찾으면
            if arr[j] < arr[minI]:
                # 제일 작은 값을 가진 인덱스를 갱신해주고
                minI = j
        # i번 인덱스에 놓기 (자리교환)
        arr[minI], arr[i] = arr[i], arr[minI]
        # 재귀호출 i+1 자리에 놓을 그 다음 작은 원소 찾으러
        selection_Sort(i + 1, N, arr)


arr = [3, 2, 6, 4, 8]
N = len(arr)
selection_Sort(0, N, arr)
print(arr)
