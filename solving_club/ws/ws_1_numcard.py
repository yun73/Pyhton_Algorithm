T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 카드 장수
    card = list(map(int, input()))  # N 개의 숫자 카드
    # 각 숫자별 카드의 개수를 센다
    # 숫자별 개수를 넣을 공간 생성
    # 숫자 자체를 인덱스 번호로 하여 숫자 정렬 따로 필요없음 이 문제에선
    # max_count 기본 0으로 해두고 개수값을 순회하며 갱신
    # 이때 max_count 를 가지는 카드의 숫자 갱신
    counts = [0] * (max(card)+1)
    for i in range(len(card)):
        counts[card[i]] += 1

    max_count = 0
    max_card = 0
    for i in range(len(counts)):
        if counts[i] >= max_count:
            max_count = counts[i]
            max_card = i

    print(f'#{tc} {max_card} {max_count}')

