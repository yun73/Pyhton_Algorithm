# N = 10 #일 때 답은 1
# N = 20 # > 3
# N = 30 # > 5
# N = 40 # > 11
# N = 50 # > 21

memo = [0] * 31
memo[1] = 1
memo[2] = 3

def paper(N):
    global memo
    i = N // 10
    if i == 1:
        return memo[i]
    if i == 2:
        return memo[i]

    if i > 2 and memo[i] == 0:
        memo[i] = paper(N - 10) + 2 * paper(N - 20)

    return memo[i]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc} {paper(N)}')


# memo = [0] * 31
# memo[1] = 1
#
# def paper(N):
#     global memo
#
#     i = N // 10
#
#     if i == 1:
#         return memo[i]
#
#     if i % 2 == 0 and memo[i] == 0:
#         memo[i] = paper(N - 10) * 2 + 1
#     elif i % 2 != 0 and memo[i] == 0:
#         memo[i] = paper(N - 10) * 2 - 1
#
#     return memo[i]
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     print(f'#{tc} {paper(N)}')
