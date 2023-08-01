T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 카드 장수
    card = list(map(int, input()))  # N 개의 숫자 카드
    # 각 숫자별 카드의 개수를 센다
    # 숫자별 개수를 넣을 공간 생성
    # 숫자 자체를 인덱스 번호로 하여 숫자 정렬 따로 필요없음 이 문제에선
    # max_count 기본 0으로 해두고 개수값을 순회하며 갱신
    # 이때 max_count 를 가지는 카드의 숫자 갱신
    counts = [0] * (max(card) + 1)
    for i in range(len(card)):
        counts[card[i]] += 1

    max_count = 0
    max_card = 0
    for i in range(len(counts)):
        if counts[i] >= max_count:
            max_count = counts[i]
            max_card = i

    print(f'#{tc} {max_card} {max_count}')



for tc in range(1, T + 1):
    N = int(input())
    numbers = input()

    # 카운트 배열 사용, 등장하는 숫자의 범윅  0 ~ 9
    # count[i] 가 의미하는 것은  number 에서 숫자 i가 등장한 횟수
    counts = [0] * 10

    for num in numbers:
        counts[int(num)] += 1  # num 등장한 횟수 1증가

    # 최대개수
    max_count = 0
    # 가장큰 수
    max_num = 0
    # 0~9 까지의 숫자들 중에서 가장 자주 등장한 숫자가 무엇인가??
    # 그리고 등장한 횟수가 같다면 그 즁애 큰거 골라서 출력

    for i in range(10):
        if counts[i] >= max_count:
            # 숫자 i의 등장횟숫가 지금까지 내가 알고있던 최대 회수보다 많으면
            # 최대값 갱신
            max_count = counts[i]
            # 가장큰 수 갱신
            max_num = i

    print(f'#{tc} {max_num} {max_count}')
