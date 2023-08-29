'''
A 대비 문제 풀기
'''
# 경사로 활주로
def check(strip, N, L):
    '''
    경사로 가능한지 체크하는 함수
    가능하면 1반환
    불가능하면 0반환
    '''
    # 경사로 가능한 곳 체크하는 리스트
    possible = [0] * N
    # 경사진데 만나기 전까지 평평한 땅 세면서 가기
    plat = 1 # 기본적으로 자기자신은 평평한 땅이므로
    # 내리막도 오르막으로 보고 처리하자
    # 앞쪽부터 보는 경우
    for i in range(N-1):
        # 일단 높이 차이 1보다 큰데 있으면 바로 0 리턴
        if abs(strip[i+1]-strip[i])>1:
            return 0

        # 1칸 올라가야 되면
        elif strip[i+1] - strip[i] == 1:
            # 지금까지 누적된 평평한 땅길이와 경사로 길이랑 비교하여 설치 가능한지 검토
            if plat >= L:
                # 경사로 설치 가능하다면 해당 지역 표시
                for j in range(L):
                    possible[i-j] += 1
            else: # 불가능하면 바로
                return 0
            # 평평한 땅 1로 초기화
            plat = 1

        elif strip[i+1] - strip[i] == 0:
            plat += 1

    plat = 1
    # 뒤쪽부터 보는 경우
    for i in range(N - 1,0,-1):
        # 일단 높이 차이 1보다 큰데 있으면 바로 0 리턴
        if abs(strip[i - 1] - strip[i]) > 1:
            return 0

        # 1칸 올라가야 되면
        elif strip[i - 1] - strip[i] == 1:
            # 지금까지 누적된 평평한 땅길이와 경사로 길이랑 비교하여 설치 가능한지 검토
            if plat >= L:
                # 경사로 설치 가능하다면 해당 지역 표시
                for j in range(L):
                    possible[i + j] += 1
            else:  # 불가능하면 바로
                return 0
            # 평평한 땅 1로 초기화
            plat = 1

        elif strip[i - 1] - strip[i] == 0:
            plat += 1

    # 여기까지 왔으면 이제 경사로 설치구간이 안겹치는지만 확인하면 됨
    if 2 in possible:
        return 0
    else:
        return 1


# N : 지형 크기, L : 경사로 가로 길이
N, L = map(int, input().split())
# 지형 높이 정보
land = [list(map(int, input().split())) for _ in range(N)]

# 경사로 가능한 곳 체크
ramp = 0
# 행 열 순회하며 판단
for r in range(N):
    # 검사할 행과 열
    row = [0]*N
    col = [0]*N
    for c in range(N):
        # 검사할 행과열에 해당하는 값들을 넣어주고
        row[c] = land[r][c]
        col[c] = land[c][r]
        # 행과 열을 경사로 건설이 가능한지 검사한다
    ramp += check(row,N,L)
    ramp += check(col,N,L)

print(ramp)

# 함수 부분을 이런식으로도 가능
def check_slope(row):
    cnt = 1
    for i in range(1, N):
        if row[i] == row[i-1]:	# 같은 높이라면
            cnt += 1
        elif row[i] - row[i-1] == 1 and cnt >= X:   # 높이 1 높아지면
            cnt = 1
        elif row[i-1] - row[i] == 1 and cnt >= 0:   # 높이 1 낮아지면
            cnt = -X + 1
        else:   # 높이 2 이상 차이나면
            return 0
    if cnt >= 0:
        return 1
    return 0

# 전치행렬을 사용해도 된다