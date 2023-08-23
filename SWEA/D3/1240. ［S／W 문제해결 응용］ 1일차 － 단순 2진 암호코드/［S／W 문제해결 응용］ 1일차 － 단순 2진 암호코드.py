
code = {'0001101': '0',
        '0011001': '1',
        '0010011': '2',
        '0111101': '3',
        '0100011': '4',
        '0110001': '5',
        '0101111': '6',
        '0111011': '7',
        '0110111': '8',
        '0001011': '9'}
T = int(input())
for tc in range(1, T + 1):
    # N : 세로크기, M : 가로크기
    N, M = map(int, input().split())
    code_list = [input() for _ in range(N)]
    password = ''
    for c in code_list:
        if '1' in c:
            # 코드의 행을 돌며 7칸 씩 끊어서
            # 모든 암호의 끝이 1임
            i = M-1
            while i >-1:
                if len(password) == 8:
                    break
                if c[i] == '1': # 여기서부터 암호코드 끝점
                    val = c[i-6:i+1]
                    if val in code.keys():
                        password += code[val]
                        i -= 7
                else:
                    i -= 1
            break
    password = password[::-1]
    sum_odd = 0
    sum_even = 0
    for i in range(0, 8, 2):
        sum_odd += int(password[i])
        sum_even += int(password[i + 1])

    if (sum_odd * 3 + sum_even) % 10 == 0:
        print(f'#{tc} {sum_odd + sum_even}')
    else:
        print(f'#{tc}', 0)
