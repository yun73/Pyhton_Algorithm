'''
도서관

- 현재 위치 : 0
- 마구 놓은 책들 : 0
- 각 책들의 원래 위치 리스트

- 모두 제 자리에 놔둘 때 드는 최소 걸음 수??

- 조건
    - 한 걸음에 좌표 한칸 씩
    - 책을 모두 놔둔 후 다시 0으로 안와도 됨
    - 한 번에 최대 M 권의 책을 들 수 있다.

- 걸음 수는 책의 위치의 왕복 거리
- 가장 먼 곳은 꼭 단일 거리로
- 가장 멀리 있는 곳은 남은 거 다 들고 가면 됨
- 각 방향에서 젤 멀리서 부터 M 개씩 들고
'''

# N : 책의 개수, M : 한번에 들 수 있는 최대 개수
N, M = map(int, input().split())
# 책들의 위치 리스트
lo = list(map(int, input().split()))
a = []
b = []
# 각 책들의 위치를 음수, 양수로 나누어 분리
for i in range(N):
    if lo[i]<0:
        a.append(-lo[i])
    else:
        b.append((lo[i]))
a.sort()
b.sort()
res = []
i = 0
for i in range(len(a)-1,-1,-M):
    res.append(a[i]*2)

for i in range(len(b)-1,-1,-M):
    res.append(b[i]*2)
# print(a[::-M])
# 리스트 슬라이싱 방법을 사용해서도 구현 가능
res.sort()

print(sum(res[:-1])+res[-1]//2)

