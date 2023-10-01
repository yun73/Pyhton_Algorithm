'''
숫자 고르기

- 첫 번쨰 줄 : 1~N 까지 순서대로
- 두 번째 줄 : 랜덤

각 차례의 숫자의 아랫주에 해당하는 숫자에 해당하는 차례를 조사하며
쭉 따라갔을 때 자기 자신으로 돌아오는 지 확인
근데 쭉 확인할 때 같이 되는 얘가 있으면 걔도 같이?
열결돠는 시작과 끝이 같으면 그 사이 얘뜰은 무조건 되는 얘들이네

- 첫째 줄에 뽑힌 정수들의 개수를 출력하고,
- 그 다음 줄부터는 뽑힌 정수들을 작은 수부터 큰 수의 순서로 한 줄에 하나씩 출력한다.
'''

def is_possible(x):

    global possible

    # 순환하는지 확인
    visit = [0] * (N + 1)
    visit[x] = 1
    # 만약 자기 자신까지 돌아오면 선택
    nx = line[x]
    # 지금까지 본 곳 담기
    stack = [x]
    while True:
        # 이미 방문한 곳에 도착했는데
        if visit[nx]:
            # 만약 출발점 값을 찾으면
            if nx == x:
                for k in range(len(stack)):
                    possible[stack[k]] = 1
                return True
            return False

        visit[nx] = 1
        stack.append(nx)
        nx = line[nx]


N = int(input())
line = [0]*(N+1)
possible = [0]*(N+1)
total = 0

for i in range(1,N+1):
    line[i] = int(input())

cnt = 0
for i in range(1,N+1):
    # 체크 안되어 있으면
    if not possible[i]:
        if is_possible(i):
            cnt += 1
        continue
    cnt += 1

print(cnt)
for i in range(1,N+1):
    if possible[i]:
        print(i)