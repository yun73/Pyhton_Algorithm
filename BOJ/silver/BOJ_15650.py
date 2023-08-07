N, M = map(int, input().split())
N_list = list(range(1,N+1))

for i in range(1<<N):
    num = []
    for j in range(N):
        if i & (1<<j):
            num.append(N_list[j])
    if len(num) == M:
        print(*num)
print()