N = int(input())
number = list(map(int, input().split()))
count = 0
for num in number:
    if num == 1:
        continue
    elif num == 2 or num == 3:
        count += 1
        continue
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            break
    else:
        count += 1

print(count)