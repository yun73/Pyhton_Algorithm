T = int(input())
for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    # P = 전체, Pa = A가 찾을 P, Pb = B가 찾을 P

    # i = 1  # 시작 페이지
    # r = P  # 끝 페이지
    # c = int((i + r) / 2)  # 중간 페이지

    def binary_search(P, page):  # P는 주어지는 전체 페이지, page는 찾는 페이지
        l = 1  # 탐색 왼쪽
        r = P  # 탐색 오른쪽 페이지
        count = 0  # 페이지 펼친 횟수
        while l <= r:  # 탐색구간이 존재, 원소 한개 이상이면 탐색하야함
            count += 1
            middle = int((l + r) / 2)
            if middle == page:  # 페이지 찾음
                return count
            elif middle > page:
                r = middle
            else:
                l = middle

        return False

    count_A = binary_search(P, Pa)
    count_B = binary_search(P, Pb)
    result = ''
    if count_A < count_B:
        result = 'A'
    elif count_A > count_B:
        result = 'B'
    else:
        result = 0

    print(f'#{tc} {result}')
