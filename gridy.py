'''
최소값 찾기

- N개의 수 : A1, A2, ..., AN
- L
- Di = A[i-L+1:i+1] 중 최소값

- D 에 저장된 수 출력
    - i ≤ 0 인 Ai는 무시하고 D를 구해야

- 무조건 끝 범위는 1 씩 차이남
- 겹치는 길이는 L 만큼

'''
import sys, heapq
input = sys.stdin.readline

N, L = map(int, input().split())
A = [0]+list(map(int, input().split()))
temp = []
heapq.heappush(temp,(A[1],1))
print(A[1], end=' ')
for i in range(2,N+1):
    heapq.heappush(temp, (A[i],i))
    # 만약 최소값의 인덱스가 지금 확인 하는 범위 밖이면 빼내기
    while temp[0][1] < i-L+1:
        heapq.heappop(temp)

    print(temp[0][0], end=' ')