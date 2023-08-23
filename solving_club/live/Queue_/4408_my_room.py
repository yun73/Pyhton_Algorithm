T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 돌아가야할 학생들의 수
    room = [0]*201

    for student in range(N):
        now, go = map(int, input().split())
        n = 0
        g = 0
        if now % 2 == 0:
            n = now//2
        else:
            n = now//2 + 1

        if go % 2 == 0:
            g = go//2
        else:
            g = go//2 + 1
        # ============위의 과정을 아래와 같이 해도 됨
        n = (now - 1) // 2
        g = (go - 1) // 2
        if n < g:
            for i in range(n, g+1):
                room[i] += 1

        elif n > g:
            for i in range(g, n+1):
                room[i] += 1
        else:
            room[n] += 1

    max_time = 0
    for time in room:
        if max_time < time:
            max_time = time

    print(f'#{tc} {max_time}')


