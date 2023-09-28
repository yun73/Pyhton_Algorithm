'''
코딩은 예쁘게

- 인덴트 : 각 줄의 탭 키 이용해 들여쓰기

- 연속된 줄을 그룹으로 선택하고, 각 줄의 앞에 탭 추가 및 삭제 가능

- 줄의 개수 : N, 각 줄의 앞에 있는 탭의 개수, 올바른 탭의 개수

- 편집 : 아래 두 명령을 모두 수행하는 것이 하나의 편집
    - 연속된 줄을 그룹으로 선택
    - 선택된 줄의 앞에 탭 1개를 추가하거나 삭제

- 풀이
    - 일단 각 줄마다 수행해야 하는 편집의 수를 조사
    - 만약 이전거 보다 편집해야 하는 횟수가 작거나 같으면 이전 편집에서 처리해줌
    - 이전거 보다 크면 이전거와의 차이만큼 더 편집해줘야 함
    - 근데 방향 즉 - 편집인지 + 편집인지도 알아야 함
    - + 랑 - 는 동시에 연산 못함
'''
# 줄의 개수
N = int(input())
# tab[0] : 현재 탭의 개수, tab[1] : 올바른 탭의 개수
tab = [list(map(int, input().split())) for _ in range(2)]
edit = [0] * N
# 모든 줄을 순회하며 올바른 탭과 현재 탭과의 차이 구해줌
for i in range(N):
    edit[i] = tab[1][i] - tab[0][i]

# 전체 결과
result = 0
# 부분 결과
res = 0
# 탭의 차이를 돌며
# 이전 편집 개수 기억
before = edit[0]
res = abs(before)
i = 1
while i<=N-1: # 모든 편집 다 할 때 까지
    now = edit[i]
    # 만약 마지막 인덱스이거나 부호가 바뀌면 즉 편집 방향이 바뀌면
    if before*now < 0:
        # 지금까지 구한 편집 횟수 결과에 더해주기
        result += res
        # 부분결과 초기화 하고
        res = abs(now)
        # 이전거 갱신하고
        before = now
        # 근데 만약 마지막이면
        if i == N-1:
            result += res
        # 다음걸로 가자
        i += 1

        continue

    # 아니라면 이전 결과와의 차이만큼 부분 결과에 더해줘
    # - 는 더 작은거 들어오면 편집횟수 늘어나고
    # + 는 더 큰거
    # 절대값이면 숫자 더 큰 거
    if abs(now) > abs(before):
        res += (abs(now) - abs(before))
        before = now
    else:
        before = now


    if i == N - 1:
        result += res

    i += 1

if N == 1:
    print(abs(edit[0]))
else:
    print(result)
    