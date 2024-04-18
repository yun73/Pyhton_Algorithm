import sys,heapq
input = sys.stdin.readline

def solve():
    N = int(input())
    arr = []
    for i in range(N):
        for num in list(map(int, input().split())):
            if len(arr) >= N:
                heapq.heappush(arr,max(num,heapq.heappop(arr)))
                continue
            heapq.heappush(arr,num)
            
    return heapq.heappop(arr)

print(solve())
