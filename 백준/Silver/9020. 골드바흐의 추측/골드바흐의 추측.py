T = int(input())
for tc in range(1,T+1):
    n = int(input())
    # 두 소수의 차가 적을 때가 우선이므로 중앙부터 탐색
    for i in range(n//2,1,-1):
        prime1 = 0
        pr1 = True
        prime2 = 0
        pr2 = True
        if i == 2:
            prime1 = i
        else:
            for p1 in range(2,int(i**0.5) + 1):
                if i % p1 == 0:
                    pr1 = False
                    break
        if n-i == 2:
            prime2 = n-i
        else:
            for p2 in range(2, int((n-i) ** 0.5) + 1):
                if (n-i) % p2 == 0:
                    pr2 = False
                    break

        if pr1 and pr2:
            prime1 = i
            prime2 = n-i
            print(prime1, prime2)
            break