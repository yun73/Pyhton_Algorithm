T = int(input())
for tc in range(1, T + 1):
    # N 자리 16진수 su
    N, su = input().split()
    # 각 자리 16진수 2진수로 변환 후 다 저장할 공간
    all = ''
    # 16진수 수들 하나씩 꺼내오기
    for i in su:
        # 16진수에서 10진수로 바꾸고
        hexsa = '0x' + i
        dec = int(hexsa, 16)
        # 이진수로 만들어서 저장할 공간
        binary = ''
        # 16진수 하나는 2진수 4칸으로 표현 가능하므로 각 자리를 4번씩 돌게
        for j in range(3, -1, -1):
            # 컴퓨터는 dec를 비트연산시 2진수인 0000 형태로 봄
            # 만약 현재 보는 16진수의 10진수 값과 같은 자리에 1이 있으면
            # & 연산은 둘다 1일 때 1 반환하므로
            if dec & (1 << j):
                binary += '1'
            else:  # 만약 해당 자리가 다르면 0 추가
                binary += '0'
        # 전체 답에 추가
        all += binary

    print(f'#{tc} {all}')