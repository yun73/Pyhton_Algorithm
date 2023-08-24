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

    result = []
    i = l - 1
    while i > -1:
        if bin_string[i] == '1':  # 여기서부터 암호코드 끝점
            for mul in range(1,30):
                if i - mul * 56 +1 > -1:
                    result.append((bin_string[i - mul * 56 + 1: i + 1], mul))
                else:
                    i -= 56
                    break
        else:
            i -= 1
    result2 = set(result)
    return result2


T = int(input())
for tc in range(1, T + 1):
    # N 세로크기, M 가로크기
    N, M = map(int, input().split())
    first = [input()[:M] for _ in range(N)]
    # 주어진 암호코드 저장하는 곳
    codelist = []
    arr = set(first)
    # 각 행에 코드가 있나 확인하고 있으면 코드 리스트에 넣어주나
    for r in arr:
        #뒤에서부터 보면서
        for i in range(M-1, -1, -1):
            # 0이 아닌 값들이 나온 순간 코드 시작
            if r[i] != '0':
                if r[:i+1] not in codelist:
                    # 내 앞에 있는 수들 전부다
                    codelist.append(r[:i+1])

                break

    total = 0
    # 코드 저장소 내에 있는 코드들 하나씩 꺼내서 다 바꾸고 암호검산 하자
    for code in codelist:
        # 2진수로 변환한 코드 얻기
        result = hextobin(code)
        for casee in result:
            binary, mul = casee
            # 이진수 길이
            bl = len(binary)
            # 숫자 하나당 길이
            interval = bl // 8
            # 코드 하나당 7의배수의 길이를 가지고 총 8개의 숫자 있음
            # 배수된 길이 만큼 끊어서 읽자
            password = []
            for i in range(bl-interval, -1, -interval):
                arrcode = ''
                cnt = 1
                # 숫자 하나에 해당하는 코드 순회
                for j in range(i+1 , i + interval):
                    if binary[j-1] == binary[j]:
                        cnt += 1
                        if j == i + interval - 1:
                            arrcode += str(cnt // mul)
                    else:
                        arrcode += str(cnt // mul)
                        cnt = 1
                        if j == i + interval - 1:
                            arrcode += str(cnt // mul)

                if arrcode in pat.keys():
                    password.append(pat[arrcode])
                else:
                    # 없으면 틀린거니까 다음거로 넘어가자
                    break

                if len(password) == 8:
                    passcode = password[::-1]
                    odd = 0
                    even = 0
                    for k in range(0, 8, 2):
                        odd += passcode[k]
                        if k+1 != 7:
                            even += passcode[k+1]

                    cal = odd * 3 +even +passcode[-1]

                    if cal%10 == 0:
                        total += sum(passcode)

                    password = []

    print(f'#{tc} {total}')