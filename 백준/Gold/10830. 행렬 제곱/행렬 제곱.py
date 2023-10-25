'''
행렬 제곱

- 행렬 A : N*N
- A의 B제곱
- A^B의 각 원소를 1,000으로 나눈 나머지를 출력

- A^5 = A^2 * A^2 * A

- A^2 = AxA => A^2[n][m] = A[n][m] + A[m][n]

'''
import sys
input = sys.stdin.readline

def mul(a,b):
    A_square = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            for i in range(N):
                A_square[r][c] += a[r][i] * b[i][c]
            A_square[r][c] %= 1000

    return A_square

def mul_square(a,b):
    if b == 1:
        return A # A의 원소는 1000 보다 작은 자연수 이므로 A = A%1000
    # 홀수이면 제곱 연산한거에 A 한번 더 곱한거를 리턴
    if b%2:
        next = mul_square(a, b // 2)
        return mul(mul(next,next),A)
    # 짝수이면 제곱연산한걸 나눈걸 리턴
    else:
        next = mul_square(a, b // 2)
        return mul(next,next)

N,B= map(int, input().split())
# A : NxM
A = [list(map(int, input().split())) for _ in range(N)]
for x in range(N):
    for y in range(N):
        A[x][y] %= 1000

res = mul_square(A,B)

for line in res:
    print(*line)
