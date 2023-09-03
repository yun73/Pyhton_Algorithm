# 16진수 숫자(0~F)
# 보물 상자의 뚜껑 시계방향
# 돌리때마다 한칸씩 회전
# 비밀번호는 보물상자 적힌 숫자로 만들 수 있는 모든 수 중 K번째로 큰 수의 십진수

T = int(input())
for tc in range(1, T + 1):
    # N 개 숫자, K 번째를 큰수
    N, K = map(int, input().split())
    num = input()

    dec_list = []

    for i in range(N // 4):
        # 한번 회전시마다의 젤 앞자리 숫자
        # 0 부터 2번 인덱스를 시작점으로 할 때
        # 한번 회전시마다의 칸마다의 시작점
        for j in range(0, N, N // 4):
            # 0 3 6 9, 1 4 7 10, 2 5 8 11
            # 0 4 8 12, 1 5 9 13, 2 6 10 14, 3 7 11 15
            # 숫자의 맨 앞자리의 인덱스
            start = i + j
            todec = ''
            for k in range(N // 4):
                # 각 칸의 숫자 인덱스들
                # 여기서 숫자 하나 만들어짐
                todec += num[(start + k) % N]
            # 숫자 하나 다 만들어지면
            dec = int(todec, 16)
            # 기존 숫자 리스트에 있는지 중복 체크하고
            if dec not in dec_list:
                # 넣어주기
                dec_list.append(dec)

    dec_list.sort(reverse=True)
    print(f'#{tc} {dec_list[K - 1]}')
