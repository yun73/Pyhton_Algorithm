# 강의실 배정
# Si 시작 Ti 끝나는 N개의 수업
# 최소의 강의실로 모든 수업 가능하게
# 수업 끝난 직후에 다음수업 시작 가능
import sys
input = sys.stdin.readline

# 수업 수
N = int(input())

# 교실 개수
classroom = 0
# 시간대
time = []
# Si, Ti
for _ in range(N):
    Si, Ti = map(int, input().split())
    time.append((Si,Ti))
# 종료시간으로 오름차순 정렬
time.sort(key = lambda x:x[1])
# 사용한 시간대인지 체크리스트
used = [0] * len(time)
# 맨 앞에서 부터 이을수 있으면 이어서 사용했다고 표시하고


# 이전 강의 종료시간
start, end = time.pop(0)
if used[t] == 0: # 아직 처리 안된 강의 이면
    # 강의 처리했다고 체크
    used[t] = 1
    # 지금 확인하는 강의 다음 강의들 다 확인해보자
    for i in range(t+1,N):
        if used[i] == 0:  # 아직 처리 안된 강의 이면
            if end == time[i][0]: # 이전 강의의 종료시간가이 현재 강의의 시작과 이어지면
                end = time[i][1] # 이전 강의의 종료시간을 현재 강의의 종료시간으로 바꿈
                used[i] = 1
    # 다 탐색하면 최대한 이을 수 있는 만큼 이어진 강의가 생긴거임
    classroom += 1
# 다 돌면 교실개수 추가하자
# 그 다음은 그 다음 시간대 부터 같은작업 반복
# 강의실의 개수 출력
print(classroom)