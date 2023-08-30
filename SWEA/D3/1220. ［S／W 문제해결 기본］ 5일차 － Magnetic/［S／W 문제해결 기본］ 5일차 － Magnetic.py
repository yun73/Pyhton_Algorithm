T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 1 : N극 , 2 : S극
    cnt = 0 # 교착 수
    
    # 열 우선순회
    for j in range(N):
        tmp = 0
        for i in range(N):
            # S극이고 N극이 먼저 나왔으면
            if arr[i][j] == 2 and tmp == 1:
                # 교착개수 하나 추가하고
                cnt += 1
                # 위에 있던 N극 교착처리 됐으니까 없다고 해줘
                tmp = 0
            # N극일 때
            elif arr[i][j] == 1:
                # N극 나왔다고 표시해줘
                tmp = 1

    print(f'#{tc} {cnt}')