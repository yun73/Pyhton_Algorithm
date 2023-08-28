# M 이상 N 이하인 소수 출력
M, N = map(int, input().split())
# 에라토스테네스의 체
is_prime = [True] * 1000001
is_prime[0] = False
is_prime[1] = False
for i in range(2,int(N**(0.5)) + 1):
    if is_prime[i]:
        j = 2
        while i*j <= N:
            is_prime[i*j] = False
            j += 1

for n in range(M,N+1):
    if is_prime[n]:
        print(n)
