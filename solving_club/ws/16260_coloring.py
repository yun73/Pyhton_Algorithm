T = int(input())

for tc in range(1, T + 1):
    arr = [[0] * 10 for _ in range(10)]
    N = int(input())  # 색칠할 영역의 개수

    purple = 0  # 영역이 겹쳐서 보라색이 된 곳의 개수

    for n in range(N):  # 영역 개수만큼 반복
        # 영역 요소들 입력값으로 받기
        r1, c1, r2, c2, color = map(int, input().split())
        # 영역 내에서 (r1,c1) (r2,c2) 는 각각 (o,o) (r2-r1, c2-c1)을 가르킨다
        # color = 1 (빨강), color = 2 (파랑)
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if arr[r][c] != color:
                    arr[r][c] += color
                if arr[r][c] == 3: # 같은 색깔의 영역 겹치지 않으므로 최대 값 3임
                    purple += 1

    print(f'#{tc} {purple}')
