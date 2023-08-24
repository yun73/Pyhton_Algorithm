import sys

sys.stdin = open("input_code.txt", "r")

pat = {
    '3211': 0,
    '2221': 1,
    '2122': 2,
    '1411': 3,
    '1132': 4,
    '1231': 5,
    '1114': 6,
    '1312': 7,
    '1213': 8,
    '3112': 9,
}


def hextobin(code):
    # 16진수를 2진수로 바꾸면 4배
    l = len(code) * 4
    # 배수
    multi = l // 56
    # 16진수 문자열을 10진수로 바꾼값
    x = int(code, 16)
    # 컴퓨터는 우리가 바꾼 10진수인 dec를 2진수로 보고 있음
    # 숫자를 다시 이진수 문자열로 바꾸자
    bin_string = ""
    # i 번째 비트를 검사해서 겨로가가 0 => i 번째 비트는 0
    # 결과가 0이 아니면 i번째 비트는 1
    for i in range(l - 1, -1, -1):
        if x & (1 << i):
            bin_string += '1'
        else:
            bin_string += '0'

    result = ''
    i = l - 1
    while i > -1:
        if bin_string[i] == '1':  # 여기서부터 암호코드 끝점
            result = bin_string[i - multi * 56 + 1: i + 1]
            i -= multi * 56
        else:
            i -= 1

    return result


T = int(input())
for tc in range(1, T + 1):
    # N 세로크기, M 가로크기
    N, M = map(int, input().split())
    arr = [input()[:M] for _ in range(N)]
    # 주어진 암호코드 저장하는 곳
    codelist = []
    # 각 행에 코드가 있나 확인하고 있으면 코드 리스트에 넣어주나
    for r in arr:
        if r != '0' * M:
            for i in range(M, -1, -1):
                if r[i] != 0:
                    code += r[i]
                else:
                    if code != '':
                        codelist.append(code[::-1])
                    code = ''
    total = 0
    # 코드 저장소 내에 있는 코드들 하나씩 꺼내서 다 바꾸고 암호검산 하자
    for code in codelist:
        # 2진수로 변환한 코드 얻기
        binary = hextobin(code)
        # 이진수 길이
        bl = len(binary)
        # 숫자 하나당 길이
        interval = bl // 8
        # 몇 배수 임??
        mul = interval // 7
        # 코드 하나당 7의배수의 길이를 가지고 총 8개의 숫자 있음
        # 배수된 길이 만큼 끊어서 읽자
        password = []
        for i in range(0, bl, interval):
            arrcode = ''
            cnt = 1
            # 숫자 하나에 해당하는 코드 순회
            for j in range(i + 1, i + interval):
                if binary[i - 1] == binary[i]:
                    cnt += 1
                else:
                    arrcode += str(cnt // mul)
                    cnt = 1

            password.append(pat[arrcode])
        odd = 0
        even = 0
        for k in range(0, 8, 2):
            odd += password[k]
            if k+1 != 7:
                even += password[k+1]

        result = odd *3 +even +password[-1]
        if result%10 == 0:
            total += sum[result]

