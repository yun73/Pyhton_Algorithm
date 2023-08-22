def inorder(p, N):  # N은 완전이진트리의 마지막 정점번호
    if p <= N:
        inorder(p * 2, N)  # 왼쪽 자식으로 이동
        print(tree[p], end='')  # 중위순회에서 할 일
        inorder(p * 2 + 1, N)  # 오른쪽 자식으로 이동


T = 10
for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)  # N번 노드까지 있는 완전이진트리
    for _ in range(N):
        arr = list(input().split())
        tree[int(arr[0])] = arr[1]
    # 중위순회
    print(f'#{tc} ', end=' ')
    inorder(1, N)  # root = 1
