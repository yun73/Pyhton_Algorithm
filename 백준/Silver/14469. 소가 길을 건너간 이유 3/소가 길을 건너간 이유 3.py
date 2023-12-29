import sys,heapq
input = sys.stdin.readline

N = int(input())
cow = []
for _ in range(N):
    arrived, time = map(int, input().split())
    heapq.heappush(cow,(arrived,time))

ans = 0
while cow:
    arrive_time, check_time = heapq.heappop(cow)
    if ans < arrive_time:
        ans = arrive_time + check_time
    else:
        ans += check_time

print(ans)