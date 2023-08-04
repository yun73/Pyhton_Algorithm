# N*N 크기의 절벽지대
# 각 셀은 지형의 높이
# 길이 x, 높이 1 인 경사로
# 높이 차이나면 무조건 경사로 써야함
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
        Differ = [0] * N
        possible = [1]
        for c in range(1, N):
            # 앞뒤 조사하면서 이동할 때 값이 다르면 인덱스 반환
            if abs(land[r][c] - land[r][c - 1]) > 1:
                break
            else:
                if land[r][c] > land[r][c - 1]:
                    Differ[c - 1] = 2
                elif land[r][c] < land[r][c - 1]:
                    Differ[c] = 1
        for i in range(N):
            if Differ[i] == 2:
                # 탐색 영역 i-x+1, i-2x+1
                if 0 <= i - X + 1 < N:
                    if 2 in Differ[(i - X + 2):i]:
                        possible.append(0)
                    if 1 in Differ[(i - X + 2):i]:
                        possible.append(0)
                    if 0 <= i - 2 * X + 2 < N:
                        if 1 in Differ[(i - 2 * X + 2):i]:
                            possible.append(0)
                else:
                    possible.append(0)

            elif Differ[i] == 1:
                # 탐색 영역 i-x+1, i-2x+1
                if 0 <= i + X - 1 < N:
                    if 1 in Differ[i:(i + X)]:
                        possible.append(0)
                    if 2 in Differ[i:(i + X)]:
                        possible.append(0)
                    if 0 <= i + 2 * X - 1 < N:
                        if 2 in Differ[i:(i + 2 * X-1)]:
                            possible.append(0)
                else:
                    possible.append(0)

        if 0 not in possible:
            airstrip += 1

    # 열 탐색
    for c in range(0, N):
        Differ = [0] * N
        possible = [1]
        for r in range(1, N):
            # 앞뒤 조사하면서 이동할 때 값이 다르면 인덱스 반환
            if abs(land[r][c] - land[r - 1][c]) > 1:
                break
            else:
                if land[r][c] > land[r - 1][c]:
                    Differ[r - 1] = 2
                elif land[r][c] < land[r - 1][c]:
                    Differ[r] = 1

        for i in range(N):
            if Differ[i] == 2:
                # 탐색 영역 i-x+1, i-2x+1
                if 0 <= i - X + 1 < N:
                    if 2 in Differ[(i - X + 2):i]:
                        possible.append(0)
                    if 1 in Differ[(i - X + 2):i]:
                        possible.append(0)
                    if 0 <= i - 2 * X + 2 < N:
                        if 1 in Differ[(i - 2 * X + 2):i]:
                            possible.append(0)
                else:
                    possible.append(0)

            elif Differ[i] == 1:
                # 탐색 영역 i-x+1, i-2x+1
                if 0 <= i + X - 1 < N:
                    if 1 in Differ[i:(i + X)]:
                        possible.append(0)
                    if 2 in Differ[i:(i + X)]:
                        possible.append(0)
                    if 0 <= i + 2 * X - 1 < N:
                        if 2 in Differ[i:(i + 2 * X - 1)]:
                            possible.append(0)
                else:
                    possible.append(0)

        if 0 not in possible:
            airstrip += 1

    print(f'#{tc} {airstrip}')
