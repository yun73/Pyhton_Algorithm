# 입국심사
# 맨 처음에 심사대 모두 비어있어
# 한심사대에 한사람만
# 가장 앞에 서있는 사람 비어있는 심사대로
# 심사 시간 최소만들기
# M : 상근이와 친구들
# N : 입국심사대 개수
# k번 심사대에 앚아있는 심사관이 심사하는데 드는시간 Tk
import sys

# 주어지는 각 심사대들의 시간리스트 time에 대해 clear_time 에 가능한지 판별하는 함수
def is_clear(times, clear_time):
    global M

    # 주어지는 완료시간 clear_time 에 대해
    # 가능한지 계산
    total = 0
    for time in times:
        total += clear_time//time

    # 만약 가능한 완료시간이면
    if total >= M:
        return True
    else:
        return False


N, M = map(int, sys.stdin.readline().split())
Time = [0] * N

# 이분 탐색 구간
start = 1e9 + 1
end = 0

for i in range(N):
    a = int(sys.stdin.readline().rstrip())
    Time[i] = a
    if end < a:
        end = a
    if start > a:
        start = a
 
end = end * M


min_clear = 1e19
while start <= end:

    # 탐색할 완료시간
    clear_time = (start+end)//2

    # 만약 해당 완료시간에 가능하다면
    if is_clear(Time, clear_time):
        # 최소값 저장해두고
        min_clear = clear_time
        # 더 작은 완료시간 조사하러 가보자
        end = clear_time - 1

    # 만약 불가능 하면 더 긴 시간에 대해서 탐색해보자
    else:
        start = clear_time + 1
    
print(min_clear)