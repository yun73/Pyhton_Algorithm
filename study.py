'''
벽부수고 이동하기

- N x M 의 행렬 맵
- 0 : 이동할 수 있는 곳, 1 : 이동할 수 없는 벽

- 상황 : (1,1)에서 (N,M)의 위치까지 최단경로로 이동
- 만약 한 개의 벽을 부수고 이동하는 것 가능
- 이동할 수 있는칸 상하좌우
- 불가능하면 -1

1. 먼저 출발점으로 부터 탐색을 하자
    - 0인부분만 탐색을 하면서 가고 각 위치까지의 최단 거리를 기록
    - 벽인 부분은
'''
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
maze = [list(map(int,input())) for _ in range(N)]