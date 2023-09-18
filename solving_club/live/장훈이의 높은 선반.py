# 장훈이의 높은 선반
def bt(r,N,height,B):
    global min_height
    # 종료 조건
    if r == N:
        if height>=B:
            if min_height > height:
                min_height = height
        return
    else:
        bt(r+1, N, height + H[r], B)
        bt(r+1, N, height, B)


T = int(input())
for tc in range(1,T+1):
    # N : 점원 수, B : 선반의 높이
    N, B = map(int, input().split())
    # 각 점원의 키 Hi
    H = list(map(int, input().split()))
    # B 이상인 경우 선반위의 물건 사용 가능
    # 탑의 높이는 탑을 쌓는 점원의 키의 합
    # 높이가 가장 낮은 탑은?
    min_height = N * 10000 + 1
    height = 0 # 처음 탑의 높이
    bt(0, N, height, B)

    result = min_height - B
    print(f'#{tc} {result}')