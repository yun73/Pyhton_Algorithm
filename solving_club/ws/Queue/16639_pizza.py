# 치즈 녹으면 화덕에서 꺼내
# N 개의 피자를 구울수 있는 화덕
# M개의 피자 주어짐
# 한바퀴 돌아왔을 때 치즈양에 따라서
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    oven = [0] * N
    front = 0 # 화덕입구
    # 처음에 화덕에 넣을 수 있는 만큼 피자를 넣어주자
    i = 0
    while i <= N-1:
        oven[i] = [i+1, pizza[i]]  # i는 피자 번호
        i += 1
    # print(oven)
    # 처음에  N 개에서의
    while len(oven) > 1:
        # 화덕 입구에 오면 피자 치즈 반감 시키기
        oven[front] = [oven[front][0], oven[front][1]//2]
        # 화덕 입구의 피자 값이 0이 되면 그 자리에 피자 추가
        if oven[front][1] == 0:
            if i < M:
                oven[front] = [i+1, pizza[i]]
                i += 1  # 피자 리스트의 남은 피자 인덱스
            else: # 피자 없으면 그냥 front 뺴버려
                oven.pop(front)
                front -= 1
                # 전체 크기 줄어 들어
                N -= 1
        front = (front + 1) % N

    last_pizza = oven[front][0]

    print(f'#{tc} {last_pizza}')

