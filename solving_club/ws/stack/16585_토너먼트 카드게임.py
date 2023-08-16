# 배열 직접 나누지 않고 인덱스만
def divide(start, end):
    # 종료조건
    if start == end: # 시작점 끝점 같아져 숫자 하나만 남으면
        return start
    # 중간점
    mid = (start + end) // 2
    # 왼쪽 부분 그룹
    left = divide(start, mid)
    # 오른쪽 부분
    right = divide(mid+1,end)

    #젤 안쪽부터 차례대로 가위바위보 승자 left right에 저장 되면서 최종 1인까지 반복됨
    return rck(left, right)

def rck(l, r):
    global card
    # 그룹 원소 1개가 되면 해당 원소로 가위가위보
    if card[l] == card[r]:
        return l  # 이긴 얘의 인덱스 반환
    elif card[l] - card[r] == 1 or card[l] - card[r] == -2:
        return l
    else:
        return r


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))

    # 시작점, 끝점
    start = 0
    end = N-1

    # divide 를 통해 왼쪽오른쪽으로 쪼개기
    # 최종적으로 1등의 인덱스를 반환해야함
    winner = divide(start, end) + 1
    # 인덱스 가 0부터 시작하므로 1추가

    print(f'#{tc} {winner}')