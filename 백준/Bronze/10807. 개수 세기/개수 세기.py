N = int(input())
Nums = map(int,input().split())
v = int(input())
cnt = 0
for num in Nums:
    if num == v:
        cnt += 1
        
print(cnt)