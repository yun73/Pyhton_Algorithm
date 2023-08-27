'''
IM 대비 문제 풀기
'''
# 개미
# 개미가 다닐 땅의 가로 세로값
w, h = map(int, input().split())
# 보기 편하게 이동하는 땅을 가로 h,세로 w인 배열로 두고 한다.
# land = [[0]*h for _ in range(w)]
# 개미의 초기 위치
p, q = map(int, input().split())
# 개미가 움직일 시간
t = int(input())
# 탐색방향
dr,dc = 1,1
# 개미가 가로나 세로의 경계에 닿으면 이동방향을 그 축에 대하여 대칭 시킨다
# 가로와 닿을 때 dr 반전시키기 = dr*-1
# 세로와 닿을 때 dc 반전시키기 = dc*-1
# 꼭지점에 닿으면 둘다 반전
while t>0: # 개미를 t시간동안 이동시킨다
    # 이동할 곳
    nr = p + dr
    nc = q + dc
    # 이동 위치가 경계 내부라면 그대로 이동
    if 0<nr<w and 0<nc<h:
        p,q = nr, nc
    # 이동위치가 가로의 양 끝에 닿으면 방향 전환
    elif nr == 0 or nr == w and 0<nc<h:
        p,q = nr,nc
        dr = -dr
    # 이동위치가 세로의 양 끝에 닿으면 방향 전환
    elif nc == 0 or nc == h and 0 < nr < w:
        p, q = nr, nc
        dc = -dc
    # 이동위치가 꼭지점이면
    elif not 0<nr<w and not 0<nc<h:
        p,q = nr,nc
        dr = -dr
        dc = -dc
    # 이동시키고 1초 감소
    t -= 1

print(p,q)

# 아니면 그냥 가로방향은 계속 좌우로 왔다갔다이고 세로는 세로로 왔다갔다이니까
# w = 5 일때
# 0 1 2 3 4 5 4 3 2 1 0
