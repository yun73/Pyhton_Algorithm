
def postorder(s):
    # if s: # s 번 노드가 있으면, 근데 이과정 무조건 맞는 말이니까
    if tree[s] in ['+', '-', '*', '/']:
        # tree[s] 값이 연산자 이면 왼쪽 아래쪽으로 내려가서 확인하고 더하자
        # L => 왼쪽 자식 방문
        left = postorder(cleft[s])  # 왼쪽 자식
        # R => 오른쪽 자식 방문
        right = postorder(cright[s])  # 오른쪽 자식
        # 왼쪽 자식 오른쪽 자식 에서 값 가져와 마지막에 부모에 있는 연산자로 계산
        # 부모값들은 연산자임
        # V => 연산과정 적용
        # tree[cleft[s]] + tree[cright[s]]
        if tree[s] == '+':
            tree[s] = left + right
        elif tree[s] == '*':
            tree[s] = left * right
        elif tree[s] == '-':
            tree[s] = left - right
        elif tree[s] == '/':
            tree[s] = left / right
        # 계산 결과 반환하여 부모에 전달
        return float(tree[s])

    else:  # 연산자가 아니라 숫자이면 그냥 값을 되돌려 주기만 하면 됨
        return float(tree[s])


T = 10
for tc in range(1, T + 1):
    # 정점의 개수
    N = int(input())
    # 주어지는 트리정보 저장소
    tree = [0] * (N + 1)
    # 완전 이진 트리 아니므로 부모 인덱스 이용하여 자식들 입력
    # 왼쪽 자식
    cleft = [0] * (N + 1)
    # 오른쪽 자식
    cright = [0] * (N + 1)

    for _ in range(N):
        info = input().split()
        # 노드의 번호
        n = int(info[0])
        # 0 : 노드의 번호
        # 1 : 연산자 or 피연산자
        # 2 : 왼쪽 자식 노드 번호
        # 3 : 오른쪽 자식 노드 번호


        # if info[1].isdigit(): .isdigit 으로 숫자인지 먼저 봐도 됨
        if info[1] in '+-*/': # 1번 자리에 연산자가 들어있으면
            tree[n] = info[1]
            # 연산자의 경우 무조건 왼쪽, 오른쪽 자식 주어지므로
            cleft[n] = int(info[2])
            cright[n] = int(info[3])

        else: # 피연산자가 들어 있으면
            tree[n] = int(info[1])

        # print(info)
    # print(tree)
    # print(cleft)
    # print(cright)

    # 루트 정점의 번호는 항상 1
    root = 1
    print(f'#{tc} {int(postorder(root))}')
