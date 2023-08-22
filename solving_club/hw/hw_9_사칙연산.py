def cal(s):

    if s <= N:
        if tree[s] in ['+', '-', '*', '/']:
            # tree[s] 값이 연산자 이면 왼쪽 아래쪽으로 내려가서 확인하고 더하자
            left = cal(2 * s)  # 왼쪽 자식
            right = cal(2 * s + 1)  # 오른쪽 자식
            # 결국에 위에서 return none이 되기전에
            # leaf문에서 여기를 탐색안하고, 이 전에 것들은 leaf값들 이용해서
            # tree 값에 값을 저장함
            if s // 2 > 0: # 젤 조상인 루트는 1이니까, 부모값들은 연산자임
                if tree[s] == '+':
                    tree[s] = tree[cleft[s]] + tree[cright[s]]
                elif tree[s] == '*':
                    tree[s] = tree[cleft[s]] * tree[cright[s]]
                elif tree[s] == '-':
                    tree[s] = tree[cleft[s]] - tree[cright[s]]
                elif tree[s] == '/':
                    tree[s] = tree[cleft[s]] / tree[cright[s]]
        # 왼쪽 자식 오른쪽 자식 에서 값 가져와 마지막에 부모에 있는 연산자로 계산
        else:
            return

T = 1
for tc in range(1, T+1):
    # 정점의 개수
    N = int(input())

    # 주어지는 트리정보 저장소
    tree = [0] * (N+1)

    cleft = [0] * (N+1)
    cright = [0] * (N+1)

    for _ in range(N):
        info = input().split()
        l = len(info)
        n = int(info[0])
        # 0 : 노드의 번호
        # 1 : 연산자 or 피연산자
        # 2 : 왼쪽 자식 노드 번호
        # 3 : 오른쪽 자식 노드 번호

        if l >= 3:
            cleft[n] = int(info[2])
            if l == 4:
                cright[n] = int(info[3])
            tree[n] = info[1]
        else:
            tree[n] = int(info[1])

        print(info)
    print(tree)
    print(cleft)
    print(cright)

    # 루트 정점의 번호는 항상 1
    root = 1
    print(f'{tc} {cal(root)}')