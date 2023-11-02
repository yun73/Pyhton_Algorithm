N = int(input())
X = list(map(int, input().split()))
new = sorted(list(set(X)))
res = {}
for i, x in enumerate(new):
    res[x] = i
for i in range(N):
    print(res[X[i]], end=' ')