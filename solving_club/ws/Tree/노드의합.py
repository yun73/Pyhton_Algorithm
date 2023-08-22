def postorder(s):

    if s<=N: # 노드번호가 범위 안에 있을 때
        if tree[s] != 0:  # 트리의 해당 노드에 값이 있으면 반환
            return tree[s]

        # 트리 안에 해당 값이 안채워져 있으면 구하자
        else:
            # 왼쪽 자식 값에 값 채워져 있으면 리턴 받아서 지금 위치 값에 저장하자
            left = postorder(2*s)
            # 오른쪽 자식 값에 값 채워져 있으면 리턴 받아서 지금 위치 값에 저장하자
            right = postorder(2 * s + 1)
            tree[s] += left
            tree[s] += right
            return tree[s]
    else:
        return 0
# def postorder(s):
#     if s > N:  # s 가 N보다 큰 경우는 그냥 리턴
#         return
#     # 자식이 있는 경우에 여기 까지옴
#     # 여기서 만약 값이 있는 leaf 문에 도달하면 아래 과정 안하고 돌아감
#     elif not tree[s]:
#         # 그렇지 않은 경우에, 즉 tree[s] 값이 없으면 그 및의 자식들 확인하러 또 가
#         postorder(2 * s)  # 왼쪽 자식
#         postorder(2 * s + 1)  # 오른쪽 자식
#         # 결국에 위에서 return none이 되기전에
#         # leaf문에서 여기를 탐색안하고, 이 전에 것들은 leaf값들 이용해서
#         # tree 값에 값을 저장함
#         if s // 2 > 0: # 젤 조상인 루트는 1이니까
#             tree[s] = tree[2 * s] + tree[2 * s + 1]


T = int(input())
for tc in range(1, T + 1):
    # N:노드의 개수, M:리프노드의 개수, L: 값을 출력할 노드번호
    N, M, L = map(int, input().split())
    # 완전 이진 트리
    tree = [0] * (N + 2)
    # 리프노드의 번호와 해당 번호의 값 주어짐
    for _ in range(M):
        leaf, val = map(int, input().split())
        tree[leaf] = val

    # 완전 이진 트리 이므로 전체 루트는 1
    root = 1

    postorder(root)
    print(f'#{tc} {tree[L]}')
