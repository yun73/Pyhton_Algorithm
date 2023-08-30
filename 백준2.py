# 강의실 배정
# 김종혜 선생님
# Si 시작 Ti 끝나는 N개의 수업
# 최소의 강의실로 모든 수업 가능하게
# 수업 끝난 직후에 다음수업 시작 가능

# 수업 수
N = int(input())

# 강의실 개수
classroom = N

# 강의 시간
time = [0] * (10**9 + 1)
# print(time)
# Si, Ti
max_time = 0
for _ in range(N):
    Si, Ti = map(int, input().split())

for i in range(Si, Ti):
    time[i] += 1

classroom = max(time)

# 강의실의 개수 출력
print(classroom)