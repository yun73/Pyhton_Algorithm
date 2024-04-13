'''
하나의 차선으로 된 다리
- n 개의 트럭 건너감
- 트럭 순서 바꿀 수 없음, 트럭 무게 같지 않을 수 있음

단위시간에 단위 길이만큼만 이동 가능

다리 길이 w
다리 위에 w 대 트럭만 동시에 올라갈 수 있음
다리 위에 올라가 있는 트럭들의 무게 합 <= L 최대하중

모든 트럭이 다리 건너는 최단 시간
트럭 하나가 다리를 건너는 시간 => w+1 초
'''
import sys
from collections import deque
input = sys.stdin.readline

n,w,L = map(int, input().split()) # n : 트럭의 수, w : 다리 길이, L : 다리 최대 하중
trucks = list(map(int, input().split()))

bridge = deque()
load = 0
time = 0

for truck in trucks:
    flag = 0
    # 다음 트럭 올라갈 수 있는 상황 만들어주기
    if len(bridge) >= w: #만약 다리 꽏찼다면 움직여주기
        load -= bridge.popleft()[0]
        flag = 1
    # 만약 다리 맨앞 차량이 나갈 때면 빼주기
    if bridge and bridge[0][1] + w == time+1:
        load -= bridge.popleft()[0]
        flag = 1

    tmp_time = 0
    while load + truck > L:
        load_now, start_time = bridge.popleft()
        load -= load_now
        tmp_time= start_time + w
        flag = 2

    # 만약 트럭 올라갈 수 있는 상태면 올려 보내기
    load += truck
    if flag == 0 or flag == 1:
        time += 1
    else:
        time = tmp_time
    bridge.append((truck, time))

if bridge:
    time = bridge[-1][1] + w

print(time)
