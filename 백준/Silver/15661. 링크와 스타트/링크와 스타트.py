# 링크와 스타트
# 스타트 팀, 링크팀
# 두 팀 인원수 같지 않아도 되지만, 한 명 이상이어야 해
# 번호 1부터 N 까지 배정
# 능력치 주어짐 S[1][2] + S[2][1] = 1 + 4 = 5
# 축구를 하러 모인 사람

# 생성된 그룹에 대해서 능력치의 합을 구해주는 함수
# 주어진 그룹 인원들 중 두명을 선택하여 능력치 가져와서 더하기
def ability(team):
    # 팀 인원이 한명이면 0 반환
    if len(team) == 1:
        return 0
    else:
        total = 0
        for i in range(len(team)):
            for j in range(len(team)):
                if i != j: # 자기자신이 아닐 때
                    # 연계되어 있는 능력치를 더해준다
                    total += S[team[i]][team[j]]
        return total


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

# 능력치 차이의 최소값
min_sub = 100000000000
# 두 팀으로 나누기
# 부분집합
for i in range(1,1<<(N-1)): # 중복제거 공집합 제외
    # 원래는 i가 부분집합이 2^N 개 인데
    # 절반 나온 뒤에는 중복 되므오 2^N-1 개만 확인해주고
    # 공집합은 볼 필요 없으니까 범위를 1부터 시작해 준다
    start = []
    link = []
    for j in range(N):
        if i&(1<<j): # 일치하는거는 start 팀에
            start.append(j)
        else: # 아니면 link 팀에
            link.append(j)

    # 가서 팀별 능력치 구하고 오기
    start_stat = ability(start)
    link_stat = ability(link)
    # 만약 최소값보다 작으면 값 갱신해줘
    if min_sub > abs(start_stat - link_stat):
        min_sub = abs(start_stat - link_stat)

print(min_sub)