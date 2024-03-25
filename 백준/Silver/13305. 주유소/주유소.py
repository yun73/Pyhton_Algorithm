'''

N 개의 도시

처음 출발 시 기름 없어서 주유소에서 기름 넣고 가야함

기름통 크기 무제한, 얼마든지 많은 기름 넣을 수 있다.

1km 마다 1리터의 기름,
각 도시마다 하나의 주유소, 리터당 가격 다를수도

제일 왼쪽에서 제일 오른쪽 도시로 이동하는 최소 비용


5 2 4 1 기름 가격
 2 3 1  거리
10 6 2     해당 도시까지 최소

앞에서 부터 현재까지 가장 쌌던 기름의 가격을 기록해두고
만약 현재 가격으로 가는 거보다 이전에 더 많이 충전해 놓은 것이 이득
'''
import sys
input = sys.stdin.readline

N = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))

total = cost[0] * road[0]
min_cost = cost[0]

for i in range(1,N-1):
    # 다음 도시까지 이동해야 할 거리
    distance = road[i]
    # 현재 도시의 기름값
    now_cost = cost[i]
    if min_cost > now_cost:
        min_cost = now_cost

    total += min_cost*distance

print(total)