# 최소 신장 트리

# 그래프에서 사이클 제거하고 모든 노드를 포함하는 트리 구성
# 가중치의 합이 최소가 되도록 만든경우 = 최소신장트리# 

# V : 0~V까지의 노드번호
# E : 간선개수
import heapq

# PRIM 알고리즘

def prim(start):
    heap = []
    # MST 포함 여부
    MST = [0]*(V+1)

    # 가중치, 접점정보 
    heapq.heappush(heap,(0,start))

    # 누적 가중치
    sum_w = 0

    while heap:
        # 가장 작은 가중치 가진얘 꺼내
        w, now = heapq.heappop(heap)

        # 이미 방문한 노드이면 continue
        if MST[now]:
            continue

        # 방문했다고 체크
        MST[now] = 1

        # 누적합
        sum_w += w

        # 현재노드에서 갈 수 있는 노드들 탐색
        for next in near[now]:
            # 이미 방문했으면 continue
            if MST[next[0]]:
                continue

            heapq.heappush(heap, (next[1], next[0]))

    return sum_w




T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    # 인접 리스트
    near = [[] for i in range(V + 1)]
    for _ in range(E):
        # 시작노드, 연결노드, 가중치
        n1, n2, w = map(int, input().split())
        # 무방향
        if (n2, w) not in near[n1]:
            near[n1].append((n2, w))
        if (n1, w) not in near[n2]:
            near[n2].append((n1, w))


    # 0번 노드부터 출발
    print(f'#{tc} {prim(0)}')



# Kruskal 알고리즘

T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    # 간선 정보
    edge = []
    for _ in range(E):
        # 시작노드, 연결노드, 가중치
        n1, n2, w = map(int, input().split())
        edge.append([n1,n2,w])

    # 가중치 기준으로 정렬
    edge.sort(key = lambda x: x[2])

    # 사이클 발생 여부를 union, find로 해결하자
    parents = [i for i in range(V+1)]

    def find_set(x):
        if parents[x] == x:
            return x

        parents[x] = find_set(parents[x])
        return parents[x]

    def union(x,y):
        x = find_set(x)
        y = find_set(y)

        if x==y:
            return
        
        if x<y:
            parents[y] = x
        else:
            parents[x] = y
    
    # 현재 방문한 정점수
    cnt = 0
    sum_weight = 0
    for n1,n2,w in edge:
        # 싸이클이 발생 안하면
        if find_set(n1) != find_set(n2):
            cnt += 1
            sum_weight += w
            union(n1,n2)
            # MST 구성이 끝나면
            if cnt == V+1:
                break

    print(f'#{tc} {sum_weight}')
   
