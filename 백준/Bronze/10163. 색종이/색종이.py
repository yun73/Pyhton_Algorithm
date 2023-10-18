'''
색종이

- 색종이 : N 개

- 색종이 차례로 주어질 때 겹치면 뒤에거는 안보임

- 평면 : 1000 x 1000 (0qjsqnxj)
- 가장 왼쪽 아래 칸의 번호와 너비, 높이를 나타내는 네 정수로
'''
import sys
input = sys.stdin.readline


N = int(input())
area=[0]
place = [[0]*1001 for _ in range(1001)]
for n in range(1,N+1):
    x, y, width, height = map(int, input().split())
    area.append((x, y, width, height))
    for nx in range(x, x+width):
        place[nx][y:(y+height)] = [n]*height

for n in range(1,N+1):
    x, y, width, height = area[n]
    res = 0
    for nx in range(x, x+width):
        res += place[nx].count(n)
    print(res)

