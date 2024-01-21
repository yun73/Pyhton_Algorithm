import sys
input = sys.stdin.readline

def find_fuel(N,M,land,land_col,fuel):
    
    # 방문 기록 저장
    visited = [[0]*M for _ in range(N)]
    
    fuel_num = 0 
    for r in range(N):
        for c in range(M):
            if not land[r][c]:
                continue
            if visited[r][c]:
                continue

            visited[r][c] = 1
            q = [(r,c)]
            # 석유덩어리 번호 지정
            cnt = 1
            while q:
                x,y = q.pop(0)
                land_col[y].add(fuel_num)
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx,ny = x+dx, y+dy
                    if 0<=nx<N and 0<=ny<M and land[nx][ny] and not visited[nx][ny]:
                        visited[nx][ny] = 1
                        q.append((nx,ny))
                        cnt += 1 
                        
            fuel[fuel_num] = cnt
            fuel_num += 1


            
def solution(land):

    # land = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
    N = len(land)
    M = len(land[0])

    # 열마다의 석유덩어리 지정
    land_col = [set() for _ in range(M)]
    # 석유 덩어리 기록
    fuel = dict()
    # 석유 덩어리 찾기 BFS
    find_fuel(N,M,land,land_col,fuel)

    # 석유 최대 값 찾기
    max_fuel = 0
    for col in range(M):
        total = 0
        # print(land_col[col])
        for fuel_num in land_col[col]:
            total += fuel[fuel_num]

        max_fuel = max(max_fuel, total)

    return max_fuel