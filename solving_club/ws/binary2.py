T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    binary = ''
    i = 0
    while N > 0:
        N *= 2 # 2를 곱해주는 거지만 사실 << 연산자랑 같은 기능
        if i > 12:
            print(f'#{tc} overflow')
            break
        if N >= 1:
            binary += '1'
            N -= 1
        else:
            binary += '0'
        i += 1
    else:
        print(f'#{tc} {binary}')
