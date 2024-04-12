import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key = lambda x:(x[1],x[0]))

before = 0
cnt = 0
for i in range(N):
    if arr[i][0] >= before:
        cnt += 1
        before = arr[i][1]

print(cnt)