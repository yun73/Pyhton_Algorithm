T = 10
for tc in range(1, T + 1):

    N = int(input())  # 건물의 개수

    # 각 건물들의 높이가 담긴 리스트(배열)
    # input() 함수는 한줄씩 읽는다.
    # split() 함수 써서 문자열을 ' ' 기준으로 자른다
    buildings = list(map(int, input().split()))

    # 조망권을 가지는 세대수
    count = 0

    # 반복문을 통해서 각 빌딩의 조망권이 확보된 세대의 개수를 세준다
    # 중첩 반복문 쓸거다

    # 중첩 반복문을 사용할 때는 밖 반복문/ 안 반복문
    # 한 빌딩의 모든 세대를 다 확인하고 다음 빌딩으로 넘어갈 것이기 떄문에
    # 밖의 반복문은 빌딩의 개수
    # 안의 반복문은 빌딩의 층수를 세는데 쓰겠다

    for i in range(2, N - 2):  # 양쪽 2칸씩은 무조건 높이가 0 => 확인할 필요 없음
        # buildings[i] = i 번째 빌딩의 높이
        height = buildings[i]
        for j in range(height, -1, -1):  # 층수는 꼭대기 부터 # 시작 = 꼭대기, 끝 = 0
            # 현재 i 번쨰 건물의 층수 j
            # j 층에서 양쪽 2칸을 확인한 다음 조망권이 있으면 count를 1씩 증가

            # 왼쪽 -1, -2 건물의 높이 확인, 오른쪽 +1, +2 높이 확인
            # 현재 j 층이 왼쪽과 오른쪽 건물의 높이보다 높아야 조망권임
            # 왼쪽 -1 => buildings[i-1]
            if j > buildings[i - 1] and j > buildings[i - 2] and j > buildings[i + 1] and j > buildings[i + 2]:
                count += 1
            else:
                # 조망권이 없는 경우  밑층은 확인 안해도 됨
                break

    print(f'#{tc} {count}')
