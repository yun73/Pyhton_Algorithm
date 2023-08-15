# 가위바위보
def rck(left, right):
    if card[left] == card[right]:
        return left
    elif card[left] - card[right] == 1 or card[left] - card[right] == -2:
        return left
    else:
        return right


# 맨 아래칸 다 비교해서 각 작은 그룹당 승자 나오면
# 승자들 끼리도 비교해줘야 함
def get_group(start, end):
    if start == end :
        return start

    mid = (start + end) // 2
    left = get_group(start, mid)
    right = get_group(mid + 1, end)

    return rck(left, right)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 인원수
    card = list(map(int, input().split()))

    start = 0
    end = N-1
    result = get_group(start, end) + 1

    print(f'#{tc} {result}')
