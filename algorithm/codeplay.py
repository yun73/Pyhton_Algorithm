def subset(i, N, s):

    if i == N:

        pass
    else:
        bit[i] = 1
        subset(i+1,N,s+arr[i])
        bit[i] = 0


T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

