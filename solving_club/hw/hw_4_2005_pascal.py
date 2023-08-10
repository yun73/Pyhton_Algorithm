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
# def pascal(N):
#     tri = [1] * N
#
#     if N == 1:
#         print(*tri)
#         return
#     if N == 2:
#         pascal(N - 1)
#         print(*tri)
#         return tri
#     # N 이 2보다 큰 경우
#     before = pascal(N - 1)
#     for i in range(1, N - 1):
#         tri[i] = before[i - 1] + before[i]
#     print(*tri)
#     return tri
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     print(f'#{tc}')
#     pascal(N)


memo = [0 for _ in range(10)]
# 1,2 번째 줄 아네
memo[0] = [1]
memo[1] = [1, 1]
# print(memo)
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # N번째 줄 모르네
    # row = [1] * N
    # N-1 번째줄 모르네

    for i in range(2, N):
        if memo[i] != 0:  # 저장된 i번째 메모가 있으면 다음거 실행
            continue
        else:  # 저장된 i 번째 메모가 없으면 i번째 메모 생성
            row = [1] * (i + 1)  # i =2 이지만 3번 째 열이므로
            for j in range(1, (i + 1) // 2 + 1):
                row[j] = memo[i - 1][j - 1] + memo[i - 1][j]
                row[i - j] = row[j]
            memo[i] = row
    # print(memo)

    print(f'#{tc}')
    for i in range(N):
        print(*memo[i])
