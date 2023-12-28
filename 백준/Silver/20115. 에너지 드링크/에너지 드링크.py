import sys
input = sys.stdin.readline

N = int(input())
drinks = sorted(list(map(float, input().split())))

for i in range(N-1):
    drinks[N-1] += drinks[i]/2

print(drinks[N-1])