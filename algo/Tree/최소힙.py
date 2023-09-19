# 최소힙
import heapq

hq = []

for i in range(10,0,-1):
    heapq.heappush(hq,i)

for i in range(10):
    print(heapq.heappop(hq), end = ' ')
print()

# 응용
heapq.heappush(hq, (4,'4등'))
heapq.heappush(hq, (1,'1등'))
heapq.heappush(hq, (2,'2등'))
heapq.heappush(hq, (3,'3등'))
# 최대 힙은 최소힙의 우선순위에 -만 붙이면 됨

for i in range(4):
    print(heapq.heappop(hq), end = ' ')
print()