
def inorder(i): # 중위순회
    global val

    if i > N :
        return
    else:
        inorder(2*i) # 왼쪽 서브트리로 이동
        Tree[i] = val
        val += 1
        inorder(2*i+1) # 오른쪽 서브트리로 이동



T = int(input())
for tc in range(1, T+1):
    # 1부터 N 까지의 자연수를 저장
    # 왼쪽 서브트리의 루트 <현재 노드 <오른쪽 서브 트리의 루트
    N = int(input())
    # 높이 N2
    # 중위순회 LVR
    Tree = [0] * (N+1)
    i = 1
    val = 1

    inorder(1)

    print(f'#{tc}',Tree[1], Tree[N//2])
