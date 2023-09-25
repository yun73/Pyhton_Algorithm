'''
벽돌 깨기

- 쏘는 횟수 : N 번

- 벽돌 : W x H / 0 : 빈공간, 나머지 숫자 : 벽돌

- 게임 규칙
    1. 구슬은 좌, 우로 => 항상 맨위 벽돌만 깨기 가능
    2. 벽돌 숫자 1~9 => 명중시 벽돌은 (상하좌우벡터) * (벽돌 적힌 숫자-1) 만큼 같이 제거
    3. 제거되는 범위 내에 벽돌 동시 제거
    4. 빈공간 생기면 밑으로 떨어짐

- 상황
    N 개의 벽돌을 떨어트려 최대한 많이 깨기
    => 남은 벽돌의 개수

- 백트래킹으로 구현??

과정
1. 구슬 떨어트릴 위치 정하기
2. 떨어트린 위치에서 연쇄작용 일어나는 곳 모두 탐색 -BFS
3. 새로운 배열로 넘겨주기
4. 없어지는 곳 0으로 바꿔주고
5. 중력에 의해 떨어짐
위 과정 반복
6. 돌아갈 때 이전에 기억하고 있던 블럭으로 초기화 하고
'''
import heapq
from copy import deepcopy

def create_block(bf_block):

    for j in range(W):
        for i in range(H-1,-1,-1):
            if not bf_block[i][j]:
                # 0 인부분 찾았는지
                find = True
                # i-1 부터 벽돌이 있는곳 찾기 시작
                for ni in range(i - 1, -1, -1):
                    if bf_block[ni][j]:
                        find = True
                        bf_block[i][j] = bf_block[ni][j]
                        bf_block[ni][j] = 0
                        break
                # 위에 벽돌이 없었으면 더이상 정리 x
                if not find:
                    break
    return bf_block

def bt(n,N,now):
    global max_count

    # 종료 조건
    if n == N:
        if max_count[n] < -now[0]:
            max_count[n] = -now[0]
        return

    # 누적 값
    acc_count = -now[0]

    pq = []
    # 1. 구슬 떨어트릴 위치 정하기
    # 터뜨릴 때 정하고 해당 위치 높이정보 및 블럭 정보도 갱신
    for c in range(W):
        # 새로운 배열
        new_block = deepcopy(now[1])
        # 깨트릴 데 있을 때 까지 가봐
        r = 0
        while r < H:
            if new_block[r][c]:
                break
            r += 1
        # 깨트릴 거 없어서 끝까지 갔으면 그냥 넘어가
        if r == H:
            continue
        # 2. 떨어트린 위치에서 연쇄작용 일어나는 곳 모두 탐색 -BFS
        pang = [(r,c,new_block[r][c])]
        count = 0
        while pang:
            y, x, brk = pang.pop(0)
            count += 1
            for i in range(brk):
                if i >= 1:
                    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    # 해당 위치의 값 만큼
                        ny, nx = y + i * dr, x + i * dc
                        if 0 <= ny < H and 0 <= nx < W and new_block[ny][nx]:
                            pang.append((ny, nx, new_block[ny][nx]))
                            new_block[ny][nx] = 0
                            count += 1
        # 새로운 누적값
        new_acc = acc_count + count
        # # 누적거리가 기존보다 작으면 버려
        # if max_count[n+1] > new_acc:
        #     continue
        # 다 탐색했으면 다음 탐색에 넘겨줄 새로운 배열을 만들어 넘겨줘
        next_block = create_block(new_block)
        # 우선순위 큐에 깰 수 있는 누적 블럭 값이랑 배열을 넣어줘
        heapq.heappush(pq, [-new_acc,next_block])


    # 우선순위에 따라 백트래킹 들어가자
    while pq:
        bt(n+1,N, heapq.heappop(pq))



T = int(input())
for tc in range(1,T+1):
    N,W,H = map(int, input().split())

    # 벽돌 정보
    block = [list(map(int, input().split())) for _ in range(H)]

    # 벽돌개수
    cnt = 0
    for r in range(H):
        for c in range(W):
            # 빈공간이면 넘어가
            if not block[r][c]:
                continue
            cnt += 1

    max_count = [0]*5
    bt(0, N, [0,block])

    print(f'#{tc} {cnt - max_count[4]}')

