
# N 개의 버스 노선
# 각 버스 노선은 A~ B 까지의 모든 정류장을 다님
#
# P 개의 버스 정류장 C1, C2, ... Cp
# 각 C의 정류장에 몇개의 노선 지나감?
# C를 지나가는 노선의 개수는
# P 개의 정류장 만큼 순회하며 C번호인 정류장이 노선 리스트에 포함 될 때 마다 +1
# 각 노선 A~B 까지를 다 합친 리스트 필요 => 각 인덱스에 놓인 값이 C 정류장 지나는 노선 개수
# ex) A1 = 1, B1 = 3, A2 = 2, B2 = 5 일때 인덱스 리스트[0,1,2,3,4,5] => [0,1,2,2,1,1]
# [0,1,2,2,1,1] C1 은 1, C2 2
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    AB = [0] * 5001

    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B + 1):
            AB[j] += 1

    P = int(input()) # 버스 정류장 개수
    # 버스 정류장 번호 리스트
    C_list = [0] * P
    for i in range(P):
        C = int(input())
        C_list[i] = C

    # C 정류장 지나는 노선의 개수 는 AB 에 이미 저장됨
    # 그걸 새로운 리스트에 받아 해당하는 번호에 대해서만 정리
    Ci = [0] * P
    for c in range(P):
        Ci[c] = AB[C_list[c]]

    P = int(input())  # 버스 정류장 개수
    # 버스 정류장 번호를 받아 바로 AB 리스트에서 찾아서 정답 리스트로 만들어도 됨
    C_list = [0] * P
    for i in range(P):
        C = int(input())
        C_list[i] = AB[C]

    print(f'#{tc}', *C_list)







