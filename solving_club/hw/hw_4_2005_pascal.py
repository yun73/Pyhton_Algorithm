'''
1. 첫 번째 줄은 항상 숫자 1이다.
2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다
'''

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#
#     tri = [[0]*N for _ in range(N)]
#     tri[0][0] = 1
#     for i in range(1,N):
#         for j in range(N):
#             if j-1 >=0:
#                 tri[i][j] += tri[i-1][j-1]
#
#             tri[i][j] += tri[i - 1][j]
#
#     print(f'#{tc}')
#     for n in range(N):
#         for k in range(n+1):
#             print(tri[n][k], end = ' ')
#         print()

# 스택 써서 해보자자
# 함수 호출로 풀라는거 같음
def pascal(n):

T= int(input())
for tc in range(1, T+1):
    N = int(input())

    tri = [[] for _ in range(N)] # 전체 결과이자 스택 저장소
    tri[0].append(1)
    for i in range(N):








