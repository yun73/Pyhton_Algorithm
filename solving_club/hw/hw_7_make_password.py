for tc in range(1, 11):
    t = int(input())
    de = [-1, -2, -3, -4, -5]
    num = list(map(int, input().split()))
    front = 0
    d = 0
    N = len(num)
    # 감소후 이동 시켰을 때 전 front 값이 0이면 그 배열을 반환
    while True:
        if num[front - 1] <= 0:
            num[front-1] = 0
            break
        # de[d] 만큼 감소시킨다음에
        num[front] += de[d]
        # deQueue 로 뒤로 이동시키자
        front = (front + 1) % N
        # 사이클 -1 뒤로 이동 ,-2,-3,-4,-5
        # de 리스트를 0부터 4까지 계속
        # 인덱스값 d라고 하면 (d+1) % 5
        d = (d + 1) % 5

    # front 가 지금 완성 배열의 맨 앞에 넣을 숫자를 가르킴
    password = []
    while len(password) < 8:
        password.append(num[front])
        front = (front + 1) % N

    print(f'#{tc}', *password)
