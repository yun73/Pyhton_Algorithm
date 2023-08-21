
def preorder(n): # 전위순회하여 n을 루트로 하는 서브트리의 노드 개수 구하자
    global node

    if n:  # 존재하는 정점이면
        preorder(cleft[n]) # 왼쪽 서브트리로 이동
        preorder(cright[n]) # 오른쪽 서브트리로 이동
        # 탐색하고 오면 노드개수 추가
        node += 1


T = int(input())
for tc in range(1,T+1):
    E, N = map(int, input().split())
    # 부모자식 노드 번호 쌍
    arr = list(map(int, input().split()))
    # 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내자
    # 점점 번호 E+1 까지
    # 부모를 인덱스로
    cleft = [0] * (E+2)
    cright = [0] * (E+2)
    # 자식을 인덱스로
    par = [0] * (E+2)
    for i in range(E):
        p, c = arr[i*2], arr[i*2 + 1]
        if cleft[p] == 0:
            cleft[p] = c
        else:
            cright[p] = c
        par[c] = p

    node = 0

    preorder(N)

    print(f'#{tc} {node}')

'''
1
5 1
2 1 2 5 1 6 5 3 6 4
'''