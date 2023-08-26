'''
IM 대비 문제 풀기
'''
# 4 개의 테스트 케이스
# 직사각형 두개씩 주어짐 공통부분 조사
for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(float, input().split())
    # 각 직사각형의 중심의 좌표
    cx_1, cy_1 = (x1+p1)/2, (y1+q1)/2
    cx_2, cy_2 = (x2+p2)/2, (y2+q2)/2
    # 각 직사각형의 가로, 세로의 절반
    w1, h1 = abs(p1-x1)/2, abs(q1-y1)/2
    w2, h2 = abs(p2-x2)/2, abs(q2-y2)/2
    # 주어진 두 점의 중심좌표로 거리를 이용하여 판별하자
    # 근데 두 직사각형의 위치관계가 상하, 좌우 일때가 있으므로 중심좌표xy의 차이를 이용
    # a : 공통부분이 직사각형인 경우
    #  두 중심좌표간의 거리가 가로합, 세로합보다 작아야 겹친다
    if abs(cx_2-cx_1) < w1+w2 and abs(cy_2-cy_1) < h1 + h2:
        print('a')

    # b : 공통부분이 선분인 경우
    # 한쪽은 거리 안에 들어오지만 다른 한쪽이 같으면 선분만 겹친다
    elif (abs(cx_2-cx_1) < w1+w2 and abs(cy_2-cy_1) == h1 + h2) or (abs(cx_2-cx_1) == w1+w2 and abs(cy_2-cy_1) < h1 + h2):
        print('b')

    # c : 공통부분이 점인 경우
    # 두 거리가 같으면 점에서 딱 만난다
    elif abs(cx_2-cx_1) == w1+w2 and abs(cy_2-cy_1) == h1 + h2:
        print('c')

    # d : 공통부분이 없는 경우
    # 중심 거리가 두 길이들보다 다 크거나, 하나는 같지만 나머지가 중심보다 클 때
    elif (abs(cx_2-cx_1) > w1+w2 and abs(cy_2-cy_1) <= h1 + h2) or (abs(cx_2-cx_1) <= w1+w2 and abs(cy_2-cy_1) > h1 + h2) or (abs(cx_2-cx_1) > w1+w2 and abs(cy_2-cy_1) > h1 + h2 ) :
        print('d')