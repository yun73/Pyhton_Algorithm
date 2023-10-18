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
area=[0]*N
place = [[-1]*1000 for _ in range(1000)]
for n in range(N):
    x, y, width, height = map(int, input().split())
    area[n] = width*height
    for i in range(width):
        for j in range(height):
            nx,ny = x+i, y+j
            if place[nx][ny] == -1:
                place[nx][ny] = n
                continue

            if place[nx][ny] != n:
                area[place[nx][ny]] -= 1
                place[nx][ny] = n

for n in range(N):
    print(area[n])