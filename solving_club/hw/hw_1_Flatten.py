# 높은 곳 상자 낮은곳으로 => 평탄화(최고점과 최저점 간격 줄이기)
# 평탄화 수행시 고, 저 차이 1 이내
# 덤프 : 가장 높은 곳 상자 낮은곳으로
# width = 100, height 1~ 100, dump_n 1 ~ 1000
# dump 이내 평탄화 완료시 그 때의 고저 차이 반환
# T = 10
T = 10
for tc in range(1, T + 1):
    N = int(input())
    box = list(map(int, input().split()))

    # N 이 0보다 크면 덤프 횟수가 남아 있는 것
    # N 이 0이 될 때까지 평탄화 작업 계속 한다 한번 할 때 마다 1씩 감소
    while N > 0:
        # 제일 높은 상자가 어디있는데?
        max_idx = 0
        # 상자의 높이 최대값
        max_height = 0
        # 제일 낮은 상자가 어디있는데?
        min_idx = 0
        # 상자의 높이 최소값
        min_height = 100

        # 가로의 길이 100 만큼 반복하면서 최대값, 최소값 찾기
        # 상자를 옮기면 높이가 변하기 때문에 그 위치도 기억해야함
        for i in range(100):
            # i 번째 상자의 높이 : box[i]
            # i 번째 상자의 높이가 지금까지 내가 알고있던 상자높이보다 높으면 갱신
            if box[i] > max_height:
                max_height = box[i]
                max_idx = i

            if box[i] < min_height:
                min_height = box[i]
                min_idx = i  # 제일 낮은 상자 위치 기억

        # 100개의 상자를 다 확인하고 나서
        # 제일 높은 위치에 있는 상자 하나를 제일 낮은 위치에 있는 곳으로 옮긴다.
        # 제일 높은 곳 높이 -1, 제일 낮은 곳 높이 +1
        box[max_idx] -= 1
        box[min_idx] += 1

        N -= 1

        # 평탄화 작업이 끝 마지막에 한번 더 구해줘야함
    max_height = 0
    min_height = 100

    for i in range(100):
        if box[i] > max_height:
            max_height = box[i]

        if box[i] < min_height:
            min_height = box[i]

    result = max_height - min_height

    print(f'{tc} {result}')

    # ====================내풀이

T = 10
for tc in range(1, T + 1):
    dump = int(input())
    box = list(map(int, input().split()))

    # 최고, 최저 박스 높이 값 설정
    max_box = 0
    min_box = 100
    # 가로 길이 100 , 최대 높이 100이므로 각 높이에 해당하는 인덱스에 개수 추가
    count = [0] * 101
    for i in range(100):
        count[box[i]] += 1  # count의 box[i] 인덱스에 개수 추가
        if max_box < box[i]:  # 반복문 도는 김에 박스 높이들 중 최대 최소값 찾기
            max_box = box[i]
        if min_box > box[i]:
            min_box = box[i]

    while dump > 0:
        if max_box - min_box < 2:
            break
        # max_box의 개수를 줄이고 낮은값의 개수 올림
        count[max_box] -= 1
        count[max_box - 1] += 1
        # min_box의 개수를 줄이고 높은 값의 개수 올림
        count[min_box] -= 1
        count[min_box + 1] += 1
        # 만약에 count[max_box]의 값이 0이 되면 max_box 값 갱시
        if count[max_box] == 0:
            max_box -= 1
        if count[min_box] == 0:
            min_box += 1
        # 위의 과정 dump 이므로
        dump -= 1

    result = max_box - min_box

    print(f'#{tc} {result}')
