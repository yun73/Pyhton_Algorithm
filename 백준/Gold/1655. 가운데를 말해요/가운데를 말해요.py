'''
가운데를 말해요

- 숫자 : N 개 차례대로 외치면
- 동생은 : N 번째 숫자까지의 중간값을 불러야 함

- 들어온 숫자와 리스트의 같과 비교하여 작은리스트, 큰 리스트 중 어디에 넣을지
- 지금까지의 불린수들의 대소관계를 알아야 하는데
- 제한 시간이 0.1초
- 그러면 넣으면서 우선순위가 부여되는 우선순위큐를 쓰자
- left는 값을 뺴서 비교할 때 큰값이 나와서 비교되야 하므로
- left : 최대힘
- right : 최소힙
'''
import sys, heapq
input = sys.stdin.readline

left = []
right = []
N = int(input())
for i in range(N):
    num = int(input())
    # len(left) >= len(right) 여야 함
    # left는 값을 뺴서 비교할 때 큰값이 나와서 비교되야 하므로 - 붙여서 넣기
    if len(left) == len(right):
        heapq.heappush(left,-num)
    else:
        heapq.heappush(right, num)

    # 모든 과정 끝나고 left의 젤 큰 숫자는 중간값이어야 함
    # 만약 오른쪽에 넣는 차례에 left에 들어갈 숫자가 들어간다면
    # 즉 중간값 보다 작은 숫자가 들어간다면 바꿔서 넣어야 함
    if right and -left[0] > right[0]:
        # 바꿀 값들 추출
        L = heapq.heappop(left)
        R = heapq.heappop(right)
        # 교체
        heapq.heappush(left, -R)
        heapq.heappush(right, -L)

    print(-left[0])