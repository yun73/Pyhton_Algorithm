import sys
input = sys.stdin.readline

cnt = int(input())
real = sorted(list(map(int, input().split())))

if cnt % 2:
    N = real[cnt//2]**2
else:
    N = real[0] * real[-1]

print(N)