# 한 조의 인원 제한 없음
# 한 사람이 여러장이 종이 제출, 여러사람이 한 사람을 지목한 경우 모두 같은 조

# 1. 집합 초기화
def make_set(x):
    p[x] = x


# 2 대표를 찾는 연산
def find_set(x):
    # 경로 압축
    if x != p[x]:
        p[x] = find_set(p[x])

    return p[x]

# 3. 두 집합을 합치는 연산
def union(x,y):
    # x 집합의 대표와 y집합의 대표를 찾기
    x = find_set(x)
    y = find_set(y)

    if y>x:
        p[x] = y
        return
    else:
        p[y] = x
        return



T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    # 신청서
    paper =list(map(int, input().split()))
    # 해당 인덱스 학생이 포함된 그룹의 대표자
    p = [0] * (N+1)
    for i in range(1,N+1):
        # 자기 자신이 대표
        p[i] = i

    for i in range(M):
        union(paper[i*2], paper[i*2+1])

    for i in range(1,N+1):
        find_set(i)

    print(f'#{tc} {len(set(p))-1}')

