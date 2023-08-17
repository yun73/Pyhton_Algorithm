def geunsonsil(r, N, K, geun):
    global count
    global check
    # 여기까지 도달하면 가능한거임
    if r == N:
        count += 1

    else:
        if geun < 500:
            return
        else:
            for c in range(N):
                if check[c] == 0:
                    geun -= K
                    check[c] = 1
                    geunsonsil(r + 1, N, K, geun + A[c])
                    geun = geun + K
                    check[c] = 0


# N 은 운동하는 일수ㅜ, K는 라루에 감소하는 중량
N, K = map(int, input().split())
A = list(map(int, input().split()))
# 운동 종류당 한번씩만 가능하니까 1차워 비트
check = [0] * len(A)
# 가능한 경우의 수
count = 0
# 초기 근육
geun = 500
geunsonsil(0, N, K, geun)
print(count)
