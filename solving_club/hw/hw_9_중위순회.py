def inorder(n):
    if n <= N:
        # 왼쪽
        inorder(n*2)  # 왼쪽 서브트리로 이동
        # 가운데 해당 문자 출력
        print(tree[n-1][1],end = '')   # visit(n)
        # 오른쪽
        inorder(n*2+1)  # 오른쪽 서브트리로 이동


T = 10
for tc in range(1, T+1):
    N = int(input())
    # 노드 번호, 해당 정점의 문자, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점 번호
    tree = [list(input().split()) for _ in range(N)]

    print(f'#{tc}', end = ' ')
    inorder(1)
    print()

