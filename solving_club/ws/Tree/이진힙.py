def hq(item):
    global last
    last += 1
    # 마지막 위치에 원소 추가
    heap[last] = item  # item = su[i], i=>1~N

    c = last  # 현재 위치가 자식노드
    p = c // 2  # 부모 위치

    # 부모노드가 존재하고, 부모 노드가 자식 노드가 작을때 까지
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 노드의 수 1~N 번 노드까지
    # 최소힙에 넣을 숫자들
    su = list(map(int, input().split()))
    # 최소힙 배열
    heap = [0] * (N + 1)
    # 마지막 저장 위치
    last = 0
    for i in range(N):
        hq(su[i])

    # 가장 마지막 노드의 조상노드들의 합
    p = N // 2
    total = 0
    while p:
        total += heap[p]
        p = p // 2

    print(f'#{tc} {total}')
