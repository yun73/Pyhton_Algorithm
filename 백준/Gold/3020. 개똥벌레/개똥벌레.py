'''

N(짝수), H : 동굴 길이, 높이

첫번째 무조건 석순 >> 종유석, 석순 번갈아가며 등장

개똥벌레
지나갈 구간 선정 후 모든 장애물 파괴

파괴해야 하는 장애물의 최소 값과
해당 구간 몇 개 인지

파괴하는 개수
- 만약 내가 석순의 뚫고 지나갈 높이를 정한다면
    - 파괴하야 하는 장애물의 개수는
        + 지금 정한 높이보다 크거나  석순의 개수
        + (동굴 높이-정한 높이) 보다 큰 종유석의 개수


- 정할 높이의 시작값과 끝값은
    - 종유석의 최단 길이, 종유석의 최고 길이



2 ≤ N ≤ 200,000, 2 ≤ H ≤ 500,000

'''
import sys
input = sys.stdin.readline

N, H = map(int, input().split())
top = [0] * (H+1)
bottom = [0] * (H+1)
path = [0] * (H+1)
for i in range(N):
    h = int(input())
    if i % 2:
        top[H-h+1] += 1
    else:
        bottom[h] += 1

# 1 2 3 4 이렇게 있으면 누적합이 1~H 까지가 아니라 H부터 1까지 역순으로 늘어남
for i in range(H-1,0,-1): # 누적 시켜야 되는데 H-1 부터 시작
    top[H-i+1] += top[H-i]
    bottom[i] += bottom[i+1]
for i in range(1,H+1):
    path[i] = top[i] + bottom[i]

path.pop(0)
cnt = 0 # 동일 구간
min_crash = min(path) # 최소 개수
for i in range(H):
    # 높이 1부터 H 까지 구간 전부 확인?? 50만인데
    if path[i] == min_crash:
        cnt += 1

print(min_crash,cnt)