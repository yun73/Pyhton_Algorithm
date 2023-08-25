'''
IM 대비 문제 풀기
'''
# 창고 다각형
# N 개의 막대, 모두 폭 1m

'''
지붕은 수평 부분과 수직 부분으로 구성되며, 모두 연결되어야 한다.
지붕의 수평 부분은 반드시 어떤 기둥의 윗면과 닿아야 한다.
지붕의 수직 부분은 반드시 어떤 기둥의 옆면과 닿아야 한다.
지붕의 가장자리는 땅에 닿아야 한다.
비가 올 때 물이 고이지 않도록 지붕의 어떤 부분도 오목하게 들어간 부분이 없어야 한다.
'''
# 창고 주인이 면적 가장 작은 창고 만들래
# 기둥의 개수 N
# 왼쪽 면 위치 : L, 높이 : H

N = int(input())
# 지표면 형성 최대 1000까지
geo = [0] * 1002
# 시작점과 끝점 만들기
start = 1000
end = 0
# 가장 높은점 입력받기
high = 0
goal = 0
# N번의 기둥 정보를 받으며 시작점과 끝점을 갱신해준다
for _ in range(N):
    L, H = map(int, input().split())
    geo[L] = H
    if start > L:
        start = L
    if end < L:
        end = L
    if high < H:
        high = H
        goal = L

# 계산된 넓이
area = 0
# 기둥 정보 받았으면 지표면을 시작점부터 끝점 까지 돌면서 바꾼다
# 양쪽에서부터 가장 큰 값을 찾으러 가자
# 가다가 중간에 나보다 큰 값 만나면 걔 높이로 넓이 계산하자
# 이전 높이
bh = geo[start]
for s in range(start, goal+1):
    # 지금 보는 칸 높이가 이전 높이보다 크다면
    # 높이 갱신하고 그걸로 면적 계산
    if geo[s] > bh:
        bh = geo[s]
        area += bh
    else: #지금 보는 칸보다 같거나 작으면 이전 높이로 계속 진행
        area += bh

# 이전 높이
bh = geo[end]
for e in range(end, goal-1, -1):
    if geo[e] > bh:
        bh = geo[e]
        area += bh
    else: #지금 보는 칸보다 같거나 작으면 이전 높이로 계속 진행
        area += bh

area -= high

print(area)
