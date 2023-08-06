import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(N)]  # 주어지는 지형정보

    # 가능한 활주로의 개수
    airstrip = 0

    # 행 우선 순회 > 활주로 가능성
    for r in range(0, N):
        left = 1
        right = 1
        possible = []
        # 경사 바꾼 곳을 + 1 하자
        slope = [0] * N
        for lc in range(1, N - 1): # 행 왼쪽부터 탐색
            if abs(land[r][lc] - land[r][lc + 1]) > 1:
                possible.append(1)
            else:
                if land[r][lc+1] > land[r][lc]:
                    if left >= X:
                        if lc - X + 1 >= 0:
                            for k in range(lc - X + 1, lc):
                                slope[k] += 1
                                left = 1
                        else:
                            possible.append(1)
                    else:
                        possible.append(1)
                elif land[r][lc + 1] == land[r][lc]:
                    left += 1
                else:
                    left = 1
        if 1 in possible:
            continue

        else:
            for rc in range(N-1, 0, -1):
                if abs(land[r][rc] - land[r][rc - 1]) > 1:
                    possible.append(1)
                else:
                    if land[r][rc - 1] > land[r][rc]:
                        if right >= X:
                            if rc + X - 1 < N:
                                for k in range(rc, rc + X):
                                    slope[k] += 1
                                    right = 1
                            else:
                                possible.append(1)
                        else:
                            possible.append(1)
                    elif land[r][rc - 1] == land[r][rc]:
                        right += 1
                    else:
                        right = 1

            if 1 in possible:
                continue
            else:
                result = 0
                for i in range(N):
                    if slope[i] < 2:
                        result += 1
                    else:
                        break

                if result == N:
                    airstrip += 1
                else:
                    continue

    # 열 우선탐색
    for c in range(0, N):
        up = 1
        down = 1
        possible = []
        # 경사 바꾼 곳을 + 1 하자
        slope = [0] * N
        for ur in range(1, N - 1):  # 위쪽부터 탐색
            if abs(land[ur+1][c] - land[ur][c]) > 1:
                possible.append(1)
            else:
                if land[ur+1][c] > land[ur][c]:
                    if up >= X:
                        if ur - X + 1 >= 0:
                            for k in range(ur - X + 1, ur):
                                slope[k] += 1
                                left = 1
                        else:
                            possible.append(1)
                    else:
                        possible.append(1)
                elif land[ur+1][c] == land[ur][c]:
                    up += 1
                else:
                    up = 1
        if 1 in possible:
            continue

        else:
            for dr in range(N - 1, 0, -1):
                if abs(land[dr-1][c] - land[dr][c]) > 1:
                    possible.append(1)
                else:
                    if land[dr-1][c] > land[dr][c]:
                        if down >= X:
                            if dr + X - 1 < N:
                                for k in range(dr, dr + X):
                                    slope[k] += 1
                                    down = 1
                            else:
                                possible.append(1)
                        else:
                            possible.append(1)
                    elif land[dr-1][c] == land[dr][c]:
                        down += 1
                    else:
                        down = 1

            if 1 in possible:
                continue
            else:
                result = 0
                for i in range(N):
                    if slope[i] < 2:
                        result += 1
                    else:
                        break

                if result == N:
                    airstrip += 1
                else:
                    continue

    print(f'#{tc} {airstrip}')
