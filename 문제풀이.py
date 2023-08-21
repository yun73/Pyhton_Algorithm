# 서쪽 N개의 사이트, 동쪽 M개의 사이트 (N ≤ M)
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # M개 다리중 N 개 선택하는 경우의 수
    # MCN
    MCN = 1
    for i in range(1,N+1):
        MCN *= (M-i+1)/i

    if M == N:
        MCN = 1

    print(int(MCN))
