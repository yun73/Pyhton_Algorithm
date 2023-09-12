# 요세푸스 문제
# N 명이 원을 이루면서 앉아있다,
# K 번째 사람 제거

N, K = map(int, input().split())

q = [i for i in range(1, N + 1)]
ans = []
arr = [i for i in range(1, N + 1)]
num = 0
for i in range(N):
    num += (K - 1)
    if num >= len(arr):
        num %= len(arr)
    ans.append(str(arr[num]))
    arr.pop(num)

print("<", ', '.join(ans), ">", sep="")
