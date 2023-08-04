# prime_factorization

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    pf = [0] * 5
    prime = [2, 3, 5, 7, 11]
    dev = 1

    while dev == 1:
        for i in range(5):
            if N % prime[i] == 0:
                N /= prime[i]
                pf[i] += 1
                break
        else:
            dev = 0

    print(f'#{tc}', *pf)