def f(i,N,s,K,rs): # rs는 남은 원소의 합
    global cnt
    if i==N:
        if s==K:
            cnt +=1
    elif s>K: # 합이 더 큰게 나와버리면
        return
    elif s+rs<K:
        return
    else:
        f(i+1, N, s+arr[i], K, rs - arr[i])
        f(i+1, N, s, K, rs - arr[i])


T = int(input())
for tc in range(1, T+1):
    N,K = map(int, input().split())
    arr = list(map(int, input().split()))
    # 재귀를 이용
    cnt = 0
    f(0,N,0,K, sum(arr))
    print(f'#{tc} {cnt}')
    # 반복문
    cnt = 0     # 합이 K가 되는 경우의 수
    for i in range(1<<N):   # 부분집합을 표시하는 i
        s = 0   # 부분집합의 합
        for j in range(N): # j 번 비트
            if i&(1<<j):    # i의 j 번 비트검사
                s += arr[j] # 0이 아니면 j 번 원소가 부분집합에 포함됨
        if s == K:
            cnt += 1
    print(f'#{tc} {cnt}')