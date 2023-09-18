# 강사님 풀이
T = int(input())

R = 1 # 오른쪽
L = 0 # 왼쪽

for tc in range(1,T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split())) # A 안에서 찾아야할 원소 리스트
    # 이진 탐색은 정렬되어 있어야 가능
    A.sort()

    # 조건에 맞으면서 A 안에서 찾은 B의 원소의 개수
    cnt = 0

    # 이진탐색 할 때 왼쪽, 오른쪽 번갈아 가며 찾은 원소의 개수
    # 내가 이전에 선택한 방향을 기억
    # 이전에 내가 선택한 방향을 또 선택하면 안된다

    for num in B:
        left = 0
        right = N-1

        # 기억할 방향, 1 = 오른쪽, 0 = 왼쪽
        dir = -1 # 처음 찾기 시작할 떄는 방향 상관 x

        while left <= right:
            mid = (left+right)//2

            # 답 찾으면 개수 증가하고 탐색중단
            if A[mid] == num:
                cnt += 1
                break
            # 답 못찾으면 구역 나누고 진행
            # 내가 찾는게 mid보다 작으면 왼쪽
            elif num < A[mid]:
                right = mid -1
                # 내가 왼쪽을 선택했다 기억
                # 내가 이전에 왼쪽 선택했으면 진행 x
                if dir == L:
                    break
                # 그게 아니먄 진행
                dir = L
            # 내가 찾는게 mid 보다 크면 오른쪽
            else:
                left = mid + 1
                # 내가 왼쪽을 선택했다 기억
                # 내가 이전에 왼쪽 선택했으면 진행 x
                if dir == R:
                    break
                # 그게 아니먄 진행
                dir = R

    print(f'#{tc} {cnt}')