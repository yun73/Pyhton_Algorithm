# x < M 이면 x + 1 아니면 1
# y < N 이면 y + 1 아니면 1
# x,y 가 몇번 째 해인지 구하여라
import sys

T = int(sys.stdin.readline())
for tc in range(1,T+1):
    M, N, x, y = map(int, sys.stdin.readline().split())

