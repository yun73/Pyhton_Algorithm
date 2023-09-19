K, N = map(int, input().split())
lan = [0]* K
max_lan = 0
for i in range(K):
    l = int(input())
    lan[i] = l
    if max_lan < l:
        max_lan = l

# lan 의 K개의 랜선을 length 길이로 잘라서
# N개 이상의 랜선을 만들 수 있는지 확인하는 함수
def cut(lan, length, N):
    cnt = 0
    for item in lan:
        cnt += item//length
    
    if cnt >= N:
        return True
    else: 
        return False

# 최소 길이 
low = 1
# 최대 길이
high = max_lan
# 길이 0부터 내가 가지고 있는 최대 랜선 길이를 이분탐색
can = 0
while low <= high:
    mid = (low+high)//2 
    # mid 값으로 랜선들을 잘랐을 때 
    # 11개 이상 만들어지면
    if cut(lan,mid,N):
        can = mid
        # 오른쪽으로 가서 길이 더 큰걸로도 되는 지 조사
        low = mid + 1

    # mid 값으로 랜선 자랐을 떄
    # 11개 이상 안만들어지면 
    else:
        # 왼쪽으로 가서 길이 줄였을 때 되는지 확인
        high = mid-1
        
    # 위 과정 반복

print(can)
