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
        # 경사 바꾼 곳을 + 1 하자
        slope = [0] * N
        for c in range(1, N - 1):
            if abs(land[r][c] - land[r][c - 1]) > 1:
                break
            else:
                if land[r][c] > land[r][c - 1]:
                    if left >= X:
                        if c - X > 0:
                            for k in range(c - X, c):
                                slope[k] += 1
                        left = 1
                    else:
                        break
                elif land[r][c] == land[r][c - 1]:
                    left += 1
                else:
                    left = 1

                if land[N - 1 - r][c] > land[N - 1 - r][c + 1]:
                    if right >= X:
                        if c + X + 1 <= N:
                            for k in range(c + 1, c + X + 1):
                                slope[k] += 1
                        right = 1
                    else:
                        break
                elif land[N - 1 - r][c] == land[N - 1 - r][c + 1]:
                    right += 1
                else:
                    right = 1
            p = 0
        for i in range(N):
            if slope[i] < 2:
                p += 1
        if p == N - 1:
            airstrip += 1

    # 열 우선 순회 > 활주로 가능성
    for r in range(0, N):
        left = 1
        right = 1
        # 경사 바꾼 곳을 + 1 하자
        slope = [0] * N
        for c in range(1, N - 1):
            # 앞뒤 조사하면서 이동할 때 값이 다르면 인덱스 반환
            if abs(land[c][r] - land[c - 1][r]) > 1:
                break
            else:
                if land[c][r] > land[c - 1][r]:
                    if left >= X:
                        if c - X >= 0:
                            for k in range(c - X, c):
                                slope[k] += 1
                        left = 1
                    else:
                        break
                elif land[c][r] == land[c - 1][r]:
                    left += 1
                else:
                    left = 1

                if land[c][N - 1 - r] > land[c + 1][N - 1 - r]:
                    if right >= X:
                        if c + X + 1 <= N:
                            for k in range(c + 1, c + X + 1):
                                slope[k] += 1
                        right = 1
                    else:
                        break
                elif land[c][N - 1 - r] == land[c + 1][N - 1 - r]:
                    right += 1
                else:
                    pass
        p = 0
        for i in range(N):
            if slope[i] < 2:
                p += 1
        if p == N - 1:
            airstrip += 1

    print(f'{tc} {airstrip}')
