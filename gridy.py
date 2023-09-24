# 정렬
# x 좌표 증가순
# 같으면 y 증가순
import sys

input = sys.stdin.readline

N = int(input())
perm = [0]*N
for i in range(N):
    x,y = map(int,input().split())
    perm[i] = (x,y)

perm.sort()

for i in range(N):
    print(f'{perm[i][0]} {perm[i][1]}')
