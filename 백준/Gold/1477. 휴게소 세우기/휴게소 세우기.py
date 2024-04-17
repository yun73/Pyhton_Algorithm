'''
휴게소 없는 구간의 길이의 최댓값을 최소로 하기

구간의 길이들을 정렬
가장 긴 구간을 찾아야 함
구간 찾으면 해당 구간 반으로 쪼개져야 함
>> 근데 이렇게 하면 무조건 반으로 쪼개서 반례 생기는데

최대인 거리를 줄이기만 하면 됨
최소인 값은 더 최소가 되든 말든 상관 없음

그러면 그 M 개 건물들의 길이가 최대 길이를 무저건 절반으로 나누는게 아닌
최소로 하는 길이를 찾아야 하니까 해당 길이를 매개변수로 이진탐색
'''
import sys
input = sys.stdin.readline

N, M ,L = map(int, input().split())
loc = [0] + sorted(map(int, input().split())) + [L]
dis = sorted( loc[i]-loc[i-1] for i in range(1,N+2))
left = 1
right = max(dis)-1
while left <= right:
    mid = (left+right)//2
    cnt = 0
    # 현재 M개 건물 사이 거리로 각 구간마다 몇개의 휴게소를 지을 수 있는 지 확인
    for i in range(1,len(loc)):
        if loc[i]-loc[i-1]-1 >= mid : # 구간 사이의 거리가 M 개 휴게소 사이 거리보다 크다면
            # 지을 수 있는 휴게소 만큼 개수 추가
            cnt += (loc[i]-loc[i-1]-1)//mid

    if cnt > M: # 만약 지을 수 있는 휴게소 개수가 더 많다면 간격 더 크게하기
        left = mid + 1
    else:
        right = mid - 1

print(left)