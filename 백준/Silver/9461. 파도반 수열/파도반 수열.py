'''
파도반 수열

- P(N) : 나선에 있는 정삼각형의 변의 길이이다.
    P(1) ~ P(10) : 1, 1, 1, 2, 2, 3, 4, 5, 7, 9

P[6] = P[5] + P[1]
P[7]= P[6] + P[2]
P[8] = P[7] + P[3]
P[9] = P[8] + P[4]
P[10] = P[9] + P[5]
P[11] = P[10] + P[6]

P[N] = P[N-1]+P[N-5]

'''
P = [0]*101
P[1] = 1
P[2] = 1
P[3] = 1
P[4] = 2
P[5] = 2
def find(n):
    global P

    if P[n]:
        return P[n]

    P[n] = find(n-1)+find(n-5)
    return P[n]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    if not P[N]:
        find(N)
    print(P[N])

