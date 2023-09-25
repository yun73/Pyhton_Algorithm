'''
공항

- 게이트 : G 개 - 1~G
- 비행기 : P 개 순서대로
- i 번째 비행기를 1번 부터 Gi 번째의이트 중 하나에 영구적으로 도킹
    - 3번 비행기 이면 1번부터 3번 게이트 중에 도킹 가능
- 비행기가 어느 게이트에도 도킹 못하면 공항 폐쇄, 이후 어떤 비행기도 도착 못함
    - 최대한 도킹 할 수 있게
- 최대 몇 대 도킹시킬 수 있음??

1. 일단 도킹 했는지 안했는지 체크해줘야 함
2. 1번 비행기 이면 1번부터 i 번 까지의 모든 비행기의 경우가 1줄어든거임
3. 그다음 2번 비행기 오면 1번부터 2번 중에 1의 경우 없어졌으니 2번만 가능
4. 만약 큰 숫자부터 오면
5. 4 번 비행기 오면 1번부터 4번중에 4번이고 4번부터 i번 까지의 비행기의 가능성 1 감소
6. 그 다음 비행기가 3번 오면
근데 이러면 n! ? 되서 시간초과 날듯

이걸 서로소집합으로 구현하게 되면
1. 초기에 각 게이트들의 리더 즉 가능한 경우는 자기자신만큼이다
2. 만약 2가 들어오면 자기자신 자리에 가능하니까 간능한 수를 1줄이고
줄인 수가 다음에 2가 들어왔을 때 1, 2 게이트중 1만 가능하다는 소리다
3. 근데 만약 그 전에 1도 들어와있었다면 루트값은 0이 되며 더이상 도킹을 하지 못하게 된다.

'''
import sys
input = sys.stdin.readline

def find(x):
    if x == park_possible[x]:
        return x
    park_possible[x] = find(park_possible[x])
    return park_possible[x]

def union(x,y):
    # a: 들어온값,b: 연결되는 값
    a = find(x)
    b = find(y)
    # 내가 지금 도킹시키고자 하는 범위 보다 한단계 작은 범위의 루트 가능성 값을 따름
    park_possible[a] = b


G = int(input())
P = int(input())

# 각 비행기 게이트의 가능성
park_possible = [i for i in range(G+1)]
# print(park_possible)
# 가능한 최대 비행기 수
cnt = 0
# P 개의 비행기 순서대로 오고
for i in range(1, P+1):
    g = int(input())
    # 더이상 도킹시킬 수 없으면 = 루트 값이 0 이면
    a = find(g)
    if find(g) == 0:
        break

    cnt += 1
    # 자기보다 한개 작은범위에 따라 내가 도킹시킬 수 있는게 달라짐
    b = a - 1
    # 둘을 같은 그룹으로 묶자
    union(a,b)
    # print(park_possible)

print(cnt)





