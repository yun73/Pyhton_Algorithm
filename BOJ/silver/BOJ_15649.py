N, M = map(int, input().split())
# 길이 M 인 수열
# 1 ~ N 까지 중에서
# 전체 정령 숫자는 NPM
all = 1
for n in range(N,N-M,-1):
    all *= n
print(all)

numbers = [[0] * M for _ in range(all)]
# numbers 는  all x M 인 2차원 배열
# [ [0 1 2 3... M-1]
#   [0 1 2 3... M-1]
#   [0 1 2 3... M-1] ]

# 첫번째 열 채우기
for r in range(N):
    for plus_r in range(all//N):
        first_row = r * (all//N) + plus_r
        numbers[first_row][0] = r + 1
# 그 다음 작은 범위 all//N//(N-1) 첫번째 구간 안에서
for r in range(N):
    for plus_r in range(all//N//(N-1)):
        second =  r * (all//N//(N-1)) + plus_r





print(numbers)


