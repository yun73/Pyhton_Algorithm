N = int(input())  # 컴퓨터의 수
co = int(input())  # 연결된 컴퓨터 쌍의 수
com = [[] for _ in range(N+1)]
for c in range(co):
    s, e = map(int, input().split())
    com[s].append(e)
    com[e].append(s)

infect = [0] * (N + 1)  # 컴퓨터 별 감염 여부
infect[1] = 1  # 1번 컴퓨터는 감염되어 있음

i = 1  # i 번 컴퓨터
stack = []  # 지나간 번호의 컴퓨터들 저장
cnt = 0  # 1번 컴퓨터에 의해 전염된 컴퓨터 수

while True:
    for pc in com[i]:  # i 번 컴퓨터에서 전염 시킬 수 있는 컴퓨터 탐색
        if infect[pc] == 0:  # 아직 전염되지 않은 컴퓨터이면
            stack.append(i)  # 찾은 컴퓨터 위치로 이동, 현재 위치 저장
            infect[pc] = 1  # 탐색 pc 전염됨
            i = pc  # pc가 다음 위치
            cnt += 1  # 전염 컴퓨터 1증가
            break  # 현재위치에서 다음 지점 찾았으니까 넘어가야됨
    else:  # 전염시킬 컴퓨터 못찾으면
        if stack:  # stack에 아직 값 있으면
            i = stack.pop()  # 이전 위치로 돌아가 다시 탐색
        else:
            break  # 다 찾았으면 종료함

print(cnt)
