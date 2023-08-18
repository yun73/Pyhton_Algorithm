# N 과 M

def bt(r, M, before):
    # r에 도달하면 수열 하나 완성 출력하자
    if r == M:
        for i in range(N):
            if choose[i] == 1:
                print(i + 1, end=' ')
        print()

    else:
        for c in range(N):
            if c > before: # 중복 안됨
                choose[c] = 1
                before = c
                bt(r + 1, M, before)
                choose[c] = 0


N, M = map(int, input().split())
# 중복없이 골라야 한다
choose = [0 for _ in range(N)]
before = -1
bt(0, M, before)
