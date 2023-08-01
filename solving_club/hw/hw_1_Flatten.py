# 높은 곳 상자 낮은곳으로 => 평탄화(최고점과 최저점 간격 줄이기)
# 평탄화 수행시 고, 저 차이 1 이내
# 덤프 : 가장 높은 곳 상자 낮은곳으로
# width = 100, height 1~ 100, dump_n 1 ~ 1000
# dump 이내 평탄화 완료시 그 때의 고저 차이 반환
# T = 10
# 맨위에서 부터 같은 행에 없으면 다음으로 넘어감
# 그걸 맨 아래서 부터 채욱기
T = 10
for tc in range(1, T + 1):
    dump = int(input())
    box_height = list(map(int, input().split()))
    count = [0] * 101  # 전체 박스 상황 알려주는 리스트

    for i in range(len(box_height)):
        # 박스를 높이별 개수로 나타냄, 자동으로 오름차순
        count[box_height[i]] += 1

    max_box = 1  # 최고점
    min_box = 100  # 최저점

    for i in range(0, 100):
        if box_height[i] > max_box:
            max_box = box_height[i]
        if box_height[i] < min_box:
            min_box = box_height[i]

    # 박스 높이별 개수에서 높이가 인덱스 count(max)는 현재 max인 값의 개수를 보여준다
    # 최대값 최소값 들이 1씩 감소, 증가 하므로 count를 이용하여 양쪽의 개수를 줄이고 중앙쪽의 개수를 올리면 된다
    # 그러므로 와일문이 조건을 만족할 때까지 max의 개수는 줄이고 min의 개수는 올린다
    # 이때 max 와 비교할 때 보면 677에서 우측부터 max는 7 7 7이어야 한다. 개수를 조작하는 거지
    # 값 자체를 바꾸는게 아니라, max를 각 인덱스 즉 높이 별로 개수를 다 소진시켰을 때 max가 변하도록 한다.
    # count(max)가 4면 dump를 하며 개수 1씩 줄임 만약 개수 0이 되면 max 다음 인덱스
    # 6777 같은 경우 max = 7 개수 3 => 0 , max = 6
    # count(min) 도 max와 같이 갱신 필요
    while dump > 0:
        if max_box - min_box <= 1:
            break
        # max 쪽 개수 조절
        count[max_box] -= 1
        count[max_box - 1] += 1
        # min 쪽 개수 조절
        count[min_box] -= 1
        count[min_box + 1] += 1
        # 만약 count(max) 개수 0이 되면 max 값 갱신
        if count[max_box] == 0:
            max_box -= 1
        # 만약 count(min) 개수 0이 되면 min 값 갱신
        if count[min_box] == 0:
            min_box += 1
        # 위의 과정이 dump 이므로 전체 제한 덤프 수에서 1만큼 감소시키기
        dump -= 1

    result = max_box - min_box

    print(f'#{tc} {result}')
