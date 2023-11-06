import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()

left = {}
right = {}
if N%2:
    le,rs = N//2, N//2 + 1
else:
    le,rs = N//2,N//2
for i in range(le):
    res = left.setdefault(S[i], 0)
    left[S[i]] += 1
for i in range(rs,N):
    res = right.setdefault(S[i], 0)
    right[S[i]] += 1

for alpha in set(S):
    l = left.setdefault(alpha,0)
    r = right.setdefault(alpha,0)
    res = l + r
    # print(alpha, res)
    if res%2:
        print('No')
        break
else:
    print('Yes')


