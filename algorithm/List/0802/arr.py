# 2차원 배열  리스트안에 리스트
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
'''
3
1 2 3
4 5 6
7 8 9
'''
'''
2차원 배열 접근
- 배열 순회 : nxm 배열의 n*m 개의 모든 원소를 빠짐없이 조사
- 행 우선 순회
# i 행의 좌표, j 열의 좌표
```for i in range(n):
    for j in range(m):
        f(arr[i][j])

- 열 우선 순회
for j in range(m): # 열
    for i in range(n): # 행
        f(arr[i][j])
        
- 지그재그 순회
for i in range(n):
    for j in range(m):
        f(arr[i][j + (m-1-2*j)*(i%2)])
         j가 0부터 3까지 일때 0 3, 1 2, 2 1, 3 0 순서로 반대로 움직이게

- 위아래 지그재그 순회
'''
N = 2  # 행의 크기
M = 4  # 열의 크기
arr = [[0, 1, 2, 3], [4, 5, 6, 7]]
for i in range(N):
    for j in range(M):
        print(arr[i][j])

arr = [[0] * M for _ in range(N)]
arr2 = [[0] * M] * N  # 이렇게 만들면 리스트 하나만 생성하고 그거를 여러번 참조하는 형태
arr[0][0] = 1
arr2[0][0] = 1
# 복사하려면 한땀 한땀 반복문 써서?
print(arr)
print(arr2)

arr = [[0, 1, 2, 3], [4, 5, 6, 7]]
max_v = 0
for i in range(N):
    row_total = 0
    for j in range(M):
        row_total += arr[i][j]
    if max_v < row_total:
        max_v = row_total

print(max_v)

'''
델타를 이용한 2차 배열 탐색 - 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색
arr[0...N-1][0...N-1] # NxN 배열
di[] => [0,1,0,-1]
dj[] => [1,0,-1,0]
for i in range(0,N-1):
    for j in range(0,N-1):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<N # 유효한 인덱스면
                f(arr[ni][nj]) 
        
'''

'''
전치행렬
# i : 행의 좌표, len(arr)
# j : 열의 좌표, len(arr[0])

for i in range(3):
    for j in range(3):
        if i < j :  # i > j 이면 아래쪽 부분 
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

'''
