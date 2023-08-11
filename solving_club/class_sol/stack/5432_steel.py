T = int(input())
for tc in range(1,T+1):
    steel = input()
    cnt = 0
    s = 0
    for i in range(len(steel)):
        if steel[i] == '(':
            cnt += 1
        else:
            if steel[i-1] == '(': # 레이저인 경우
                cnt -= 1
                s += cnt
            else: # 쇠막대 끝나는경우
                cnt -= 1
                s += 1

    print(f'#{tc} {s}')