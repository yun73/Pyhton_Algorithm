import sys,heapq
input = sys.stdin.readline

def solve():
    N = int(input())
    arr = []
    for i in range(N):
        li = list(map(int, input().split()))
        for num in li:
            if len(arr) >= N:
                if arr[0] < num:
                    heapq.heappop(arr)
                    heapq.heappush(arr,num)
                continue
            heapq.heappush(arr,num)

    return heapq.heappop(arr)

print(solve())
