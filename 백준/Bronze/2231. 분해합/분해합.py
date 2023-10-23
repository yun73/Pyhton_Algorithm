N = int(input())
for M in range(N//2,N):
    part_sum = 0
    for m in str(M):
        part_sum += int(m)
    if M + part_sum == N:
        print(M)
        break
else:
    print(0)
