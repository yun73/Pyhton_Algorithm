'''
코딩은 예쁘게

- 인덴트 : 각 줄의 탭 키 이용해 들여쓰기

- 연속된 줄을 그룹으로 선택하고, 각 줄의 앞에 탭 추가 및 삭제 가능

- 줄의 개수 : N, 각 줄의 앞에 있는 탭의 개수, 올바른 탭의 개수

- 편집 : 아래 두 명령을 모두 수행하는 것이 하나의 편집
    - 연속된 줄을 그룹으로 선택
    - 선택된 줄의 앞에 탭 1개를 추가하거나 삭제

-
'''
# 줄의 개수
N = int(input())
# tab[0] : 현재 탭의 개수, tab[1] : 올바른 탭의 개수
tab = [list(map(int, input().split())) for _ in range(2)]
arr = [0] * N
# 모든 줄을 순회하며 올바른 탭과 현재 탭과의 차이 구해줌
for i in range(N):
    arr[i] = tab[1][i] - tab[0][i]
print(arr)

result = 0
# 탭의 차이를 돌며
# 이전 편집 개수 기억
before = arr[0]
result += abs(before)
for i in range(1,N):
    # 현재보는값 0 기준으로
    now = arr[i]
    # 이전 값보다 차이 적거나 같은 거 나오면 이전거에서 해줬으니까 건너뛰기
    if now <= before:
        before = now
        continue
    # 큰 거 나오면 그 차이만큼 해주기
    else:
        result += now - before
        before = now

print(result)