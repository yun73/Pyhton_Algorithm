'''
IM 대비 문제 풀기
'''
# 해당 위치를 방문하면 1로 표시하고, 또왔을 때 1이 차있으면 중복 면적이라는 것
arr = [[0] * 101 for _ in range(101)]
area = 0
for _ in range(4):
    r1, c1, r2, c2 = map(int, input().split())
    for r in range(r1, r2):
        for c in range(c1, c2):
            # 주어진 직사각형 범위 순회
            # 해당 위치를 방문한 적이 없으면 면적 추가
            if arr[r][c] == 0:
                # 해당 위치 방문했다고 표시
                arr[r][c] = 1
                area += 1

print(area)