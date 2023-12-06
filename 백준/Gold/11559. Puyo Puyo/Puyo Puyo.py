import sys
from collections import deque

input = sys.stdin.readline

def bomb():
    is_bomb = False
    visited = [[0]*6 for _ in range(12)]

    for r in range(11,-1,-1):
        for c in range(6):
            # 만약 뿌요들이 아니거나 이미 방문한 뿌요이면 넘어가기
            if arr[r][c] == '.' or visited[r][c]:
                continue
            # 뿌요들이면 bfs 탐색
            visited[r][c] = 1
            q = [(r,c)]
            puyo = [(r,c)]
            while q:
                x,y = q.pop(0)
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx,ny= x+dx ,y+dy
                    if 0<=nx<12 and 0<=ny<6 and not visited[nx][ny] and arr[nx][ny] == arr[x][y]:
                        visited[nx][ny] = 1
                        q.append((nx,ny))
                        puyo.append((nx,ny))
            # 만약 Puyo 들의 개수가 4개 이상이면
            if len(puyo)>=4:
                is_bomb = True
                while puyo:
                    i,j = puyo.pop(0)
                    arr[i][j] = '.'

    return is_bomb

def fall():
    for c in range(6):
        que = []
        start = 0
        # 첫번쨰로 나오는 puyo 찾기
        check=0
        for r in range(12):
            if arr[r][c] != '.':
                if check == 0:
                    start=r
                    check+=1
                que.append(arr[r][c])
        for fill in range(start,12):
            # 끝에가 남게되는 경우라면
            if fill + len(que) < 12:
                arr[fill][c] = '.'
                continue
            else:
                arr[fill][c] = que.pop(0)

arr = [list(input().rstrip()) for _ in range(12)]

cnt = 0
while True:
    if bomb(): # 만약 터졌으면
        fall() # 얘들 다 떨어지는 거 구현
        cnt += 1 # 연쇄횟수 추가
        # for line in arr:
        #     print(*line)
        # print(f'{cnt}연쇄 ===========')
    else:
        break

print(cnt)