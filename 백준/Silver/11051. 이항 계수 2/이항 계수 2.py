'''
이항계수
(n \ k) = nCk = n!/(n-k)!k!

(n \ k) = (n \ n-k)
(n \ k) = (n -1 \ k) + (n-1\k-1)
k = 0~n까지 sum(n\k) = 2^n

'''

def BC(n,k):
    global visited
    if visited[n][k]:
        return visited[n][k]

    if k == 0 or n == k:
        visited[n][k] = 1
        return visited[n][k]

    if k == 1:
        visited[n][k] = n%10007
        return visited[n][k]

    visited[n][k] = (BC(n-1,k) + BC(n-1,k-1))%10007
    return visited[n][k]



N, K = map(int, input().split())
visited = [[0]*(K+1) for _ in range(N+1)]
BC(N,K)
print(visited[N][K])