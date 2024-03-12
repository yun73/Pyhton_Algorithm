'''
진우의 달 여행 (Small)




'''

import sys
input = sys.stdin.readline

di = [(1,-1),(1,0),(1,1)]

def backt(n,now_m,now, before): # n : 0~N ,now 현재 코스트, before 이전에 온 방향
    global min_cost

    # 만약 우주에 도착 했다면
    if n == N:
        min_cost = min(min_cost,now)
        return
    # 만약 현재 비용이 최소 비용 보다 크다면 해당 길은 가지 않기
    if now >= min_cost:
        return

    # n 행에서 갈 수 있는 방향으로 탐색 후 갔다 오기
    for go,d in enumerate(di):
        next_m = now_m + d[1]
        if 0 <= next_m < M and go != before: # 갈수 있는 범위 라면
            backt(n+1,next_m,now+arr[n+1][next_m],go)


N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.append([0]*M)

min_cost = 601

for m, start in enumerate(arr[0]):
    backt(0,m,start,-1)

print(min_cost)