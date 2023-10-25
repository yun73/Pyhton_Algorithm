'''
행렬 곱셈

N*M크기의 행렬 A와 M*K크기의 행렬 B가 주어졌을 때, 두 행렬을 곱하는 프로그램


'''
import sys
input = sys.stdin.readline

N,M= map(int, input().split())
# A : NxM
A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
# B : MxK
B = [list(map(int, input().split())) for _ in range(M)]

# 행렬 곱셈
# M 은 같이 쓸수 있으니까 3중 반복문?
# A x B = NxM x MxK = NxK
# 즉 새로운 배열의 크기는 NxK
C = [[0]*K for _ in range(N)]
for n in range(N):
    for m in range(M):
        for k in range(K):
            C[n][k] += A[n][m] * B[m][k]

for line in C:
    print(*line)
