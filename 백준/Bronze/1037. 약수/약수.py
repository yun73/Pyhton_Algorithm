import sys
input = sys.stdin.readline

cnt = int(input())
real = sorted(list(map(int, input().split())))

N = real[0] * real[-1]

print(N)