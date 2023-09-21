

# N : 동물 수, M : 사대 수 ,L : 사정거리
M, N, L = map(int,input().split())
# 사대위치
gun = list(map(int, input().split()))
gun.sort()

# 잡는 개수
catch = 0
# 동물 위치
for i in range(N):
    x,y = map(int, input().split())
    # 일단 입력 받으면서 사정거리 밖에 있는 얘들은 받지마
    if y > L:
        continue
    left = 0
    right = len(gun)-1
    mid = 0
    idx = 0
    # 동물 위치를 기준으로 잡힐수 있는 범위를 이분탐색해서
    # 영역내에좌표가 존재하는지
    # 잡힐 수 있는 범위 시작부분
    s = x + y - L
    # 끝 부분
    e = x - y + L
    # 사대 리스트의 인덱스를 이분탐색
    left, right = 0, M - 1
    while left <= right:
        # 인덱스
        mid = (left + right) // 2
        # 해당 인덱스의 사대의 x값이 영역 안에 있는지 확인
        if gun[mid] >= s and gun[mid] <= e:
            catch += 1
            break
        # 현재 사대 위치가 영역 오른쪽에 있으면
        elif gun[mid] > e:
            right = mid - 1
        else:
            left = mid + 1


print(catch)