import heapq

def dijkstra(start_x,start_y):
    heap = []

    for i in range(4):
        visited[start_y][start_x][i] = 0
        nx,ny =start_x+d[i][0], start_y+d[i][1]
        if 0<=ny<H and 0<=nx<W and li[ny][nx] != '*':
            visited[ny][nx][i] = 0
            heapq.heappush(heap, (0,i,nx,ny))

    while heap:
        mir,dd,x,y = heapq.heappop(heap)
        if li[y][x] == 'C' and (y,x) == (end[1],end[0]):
            return

        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            if dd == i:
                mirror = 0
            else:
                mirror = 1

            if 0<=nx<W and 0<=ny<H and li[ny][nx] != '*':
                if visited[ny][nx][i] <= mir + mirror:
                    continue
                visited[ny][nx][i] = mir + mirror
                heapq.heappush(heap,(mir + mirror,i,nx,ny))



d = [(1,0),(0,1),(-1,0),(0,-1)]
W,H = map(int,input().split())
li = [list(input()) for _ in range(H)]

find = 0
for y in range(H):
    for x in range(W):
        if li[y][x] == 'C':
            if find == 0:
                start = [x,y]
                find +=1
            elif find == 1:
                end = [x,y]


INF = int(1e9)
visited = [[[INF]*4 for _ in range(W)] for _ in range(H)]

# print(visited)

dijkstra(start[0],start[1])

res = min(visited[end[1]][end[0]])
print(res)