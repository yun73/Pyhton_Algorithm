N,X = map(int, input().split())
nums = map(int, input().split())
for num in nums:
    if num < X:
        print(num, end=' ')