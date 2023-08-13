 # 탐색을 한방향으로 쭉 가다가 다 탐색시 마지막 갈림길로 가서 다른방향으로 또 탐색
# 최종적으로 모든 정점을 방문하는 순회방법
# 스택을 이용하는 탐색 방법 아님!! 도구로 스택을 사용할 뿐
# 1. 빠짐없이, 중복없이

# 갈곳이 없어서 뒷걸음질 친다고 생각 - pop 하는 과정

# 연습문제 3
'''
1 > 2 스택에 저장후 이동 [1]
> 4로 갈 떄 stack = [1,2]
6 으로 가면 [1,2,4] 거쳐간 곳을 저장
5로가면 [1,2,4,6]
갈 데 이제 없다
다시 뒷걸음
6 pop 1,2,4
6의 위치에서 다른 방향 탐색하고
있으면 7로 이동 [1,2,4 ,6] 6을 거쳐 7ㄹ로 간거니까 pop한거 다시 추가
7지나 3으로 이동 [1,2,4,6,7]
탐색 끝남 하나씩 pop 하면서 각각의 길에서 갈 수 있는 곳 탐색 없으면 계속 pop
stack이 빈 스택이 되면 모든 경로 찾은 거임
'''
'''
V E # 정점, 이어지는 점
v1 w1 v2 w2  
>>> 저장방식
2차원 배열에 모든 연결관계를 입력, 
2차원 배열로 각 정점 번호에 해당하는 인덱스에 연결된 점들을 리스트로 저장, 인접 리스트
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def dfs(n, V, adj_m):
    stack = []  # stack 생성
    visited = [0] * (V + 1)  # visited 생성
    visited[n] = 1  # 시작점 방문 표시
    print(n)  # do[n]
    while True:
        for w in range(1, V + 1):  # 현재 정점 n에 인접하고 미방문 w 찾기
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n)  # push(v), v = w
                n = w
                print(n)  # do(w)
                visited[n] = 1  # w 방문 표시
                break  # for w, n에 인접인 w 찾은 경우
        else:
            if stack:  # 스택에 지나온 정점이 남아있으면
                n = stack.pop()  # pop() 해서 다시 다른 w 찾을 n 준비
            else:  # 스택이 비어있으면
                break  # while True 탐색끝

    return


V, E = map(int, input().split())  # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))
# 인접 매트릭스
adj_m = [[0] * (V + 1) for _ in range(V + 1)]
for i in range(E):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

dfs(1, V, adj_m)
