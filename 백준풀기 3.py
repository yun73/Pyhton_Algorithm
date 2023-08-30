def paring(food):
    total = 0
    for i in range(len(food)):
        for j in range(i+1, len(food)):
            total += S[food[i]][food[j]]
            total += S[food[j]][food[i]]
    return total

def f(i, N, K):  # i 이전에 고른개수, N개에서 K개를 고르는 순열
    global min_sub

    if i == K:  # 순열 완성 : K개를 모두 고른 경우
        food_A = p
        food_B = []
        for b in range(N):
            if b not in p:
                food_B.append(b)
        A_taste = paring(food_A)
        B_taste = paring(food_B)
        # 만약 최소값보다 작으면 값 갱신해줘
        if min_sub > abs(A_taste - B_taste):
            min_sub = abs(A_taste - B_taste)

        return
    else:  # p[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j] == 0:  # 아직 사용되기 전이면
                p[i] = j
                used[j] = 1
                f(i + 1, N, K)
                used[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    K = N//2  # K개를 골라 만드는 순열
    used = [0] * N  # 이미 사용한
    p = [0] * K
    # 맛 차이의 최소값
    min_sub = 100000000
    f(0, N, K)

    print(f'#{tc} {min_sub}')