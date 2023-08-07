# 2보다 큰 모든 짝수는 두 소수의 합 = 골드바흐
# 골드바흐 파티션
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    # 두 소수의 차가 적을 때가 우선이므로 중앙부터 탐색
    for i in range(n//2,1,-1):
        prime1 = 0  # 소수 1
        pr1 = True  # i 가 소수가 아닐 때 False로 바뀜
        prime2 = 0  # 소수 1과 더했을 때 n 나오는 소수 2
        pr2 = True  # n-i 가 소수가 아닐 때 False로 바뀜
        if i == 2: # i가 2인 경우는 n-i에 대해서로 바로 넘어감, 소수판별시 2만 예외로 걸림
            pass
        else:
            for p1 in range(2,int(i**0.5) + 1): # 제곱근 까지만 검색 49과 같은 경우 제곱근을 가지므로 +1로 탐색
                if i % p1 == 0: # 차례대로 나누다가
                    pr1 = False  # 나눠지면 소수1은 False
                    break   # 더볼 거 없이 종료
        if n-i == 2: # 앞의 과정과 마찬가지
            pass
        else:
            for p2 in range(2, int((n-i) ** 0.5) + 1): # 위와 같은 과정
                if (n-i) % p2 == 0:
                    pr2 = False
                    break

        if pr1 and pr2: # i, n-i 둘 다 소수이면
            prime1 = i
            prime2 = n-i
            print(prime1, prime2)
            break # 다른 소수 쌍이 나오지 않게 두 소수의 차이가 최소일 때 스탑



