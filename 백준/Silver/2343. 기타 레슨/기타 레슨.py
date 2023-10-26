'''
기타 레슨

- 블루레이 : M개
- 강의 : N 개
    - 강의 순서대로 주어짐

- N개를 M 개로 쪼개야 한다
- 강의 시간이 쭉 오르는게 아니라 막 섞임
- 그냥 이분탐색을 해버리면 왼쪽을 조사한 후 오른쪽을 갈 수가 없음
- mid 값을 그냥 블루레이의 최소 크기로 해야함
- 블루레이 크기를 탐색 범위로 하자 최소0, 최대 10000*100000
- 주어진 데이터에서는 max(Nli), sum(Nli)
- 이렇게 할 경우 현재 mid 만큼의 합을 가지는 구간의 끝이 어딘지 모르니까
-앞에서 부터 계산하면서 해당 구간을 찾아줘야 해

- 근데 만약 구간이 M 개보다 적다면 구간을 더 나누기 위해 end 값을 mid-1로 줄여야 함
- 구간이 많아지는 경우는 start를 mid+1로 올려서 탐색

- 구간 조사 방법은 배열 순회하면서 덧셈값 이 mid보다 커지는 순간 구간 개수 추가해주고
- total을 초기화
'''
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
Nli = list(map(int, input().split()))
total = sum(Nli)
res = sum(Nli)
left,right = max(Nli), sum(Nli)
while left <= right:
    mid = (left+right)//2

    sub = 0
    group = 1
    check = total
    # 구간 나누기
    for n in Nli:
        # 남은거 다합해도 mid 안되면 그냥 빠져 나오기
        if check < mid:
            break
        if sub + n > mid:
            group += 1
            check -= sub
            sub = 0
        sub += n

    # 구간 개수 따라서 left, right  조작
    if group <= M: # 그룹개수가 적으면 더 나누러
        # 같은 경우도 더 적은 경우 되나 확인
        res = mid
        right = mid - 1
    else:
        left = mid + 1

print(res)