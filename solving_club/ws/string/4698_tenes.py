n = 1000000  # 최대로 들어올 수 있는 수
# 소수 리스트 만들기
is_prime = [True for i in range(n + 1)]
is_prime[0] = False
is_prime[1] = False
for i in range(2, int((n+1)**0.5)+1):
    if is_prime[i]:  # i가 소수인 경우
        # i를 제외한 모든 i의 배수를 소수가 아니라고 체크
        j = 2
        while i * j <= n:
            is_prime[i * j] = False
            j += 1
# 실행시간 조건에서 미리 다 구해놓고 행당범위내에 특별한 소수 있는지만 조사

T = int(input())
for tc in range(1, T + 1):
    D, A, B = map(int, input().split())

    # 소수 리스트 만들기
    is_prime = [True] * (B + 1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(B ** 0.5) + 1):
        if is_prime[i]:  # i가 소수인 경우
            # i를 제외한 모든 i의 배수를 소수가 아니라고 체크
            j = 2
            while i * j <= B:
                is_prime[i * j] = False
                j += 1

    special = 0  # 특별한 소수의 개수

    for i in range(A, B + 1):
        if is_prime[i]:
            if str(D) in str(i):  # 이렇게 안하면 %. // 이용해서 하나하나 비교해저 나오면 특별한 소수
                special += 1

    print(f'#{tc} {special}')
