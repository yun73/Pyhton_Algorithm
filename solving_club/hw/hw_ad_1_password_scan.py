import sys

sys.stdin = open("input_code.txt", "r")

pat = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}

binbyhex = {'0': '0000',
            '1': '0001',
            '2': '0010',
            '3': '0011',
            '4': '0100',
            '5': '0101',
            '6': '0110',
            '7': '0111',
            '8': '1000',
            '9': '1001',
            'A': '1010',
            'B': '1011',
            'C': '1100',
            'D': '1101',
            'E': '1110',
            'F': '1111'}

T = int(input())
for tc in range(1, T + 1):
    # N 세로크기, M 가로크기
    N, M = map(int, input().split())
    arr = list(set([input()[:M] for _ in range(N)]))
    # 코드 중복체크 방지
    dup_check = []
    total = 0
    # 각 행에 코드가 있나 확인하고 있으면 코드 리스트에 넣어주나
    for r in arr:
        # 2진수로 변환한 코드 얻기
        binary = ''
        for c in r:
            binary += binbyhex[c]

        if '1' not in binary:
            continue

        else:
            # 뒤에서 부터 확인하다 1 나오면 암호코드 시작
            # 0과 1의 비율
            ratio = [0] * 4  # 각 자리는 0101 의 비율을 저장
            # 필요없는 문자열 없애기, 모든 암호코드는 마지막이 1로 끝나니까
            binary = binary.rstrip('0')

            l = len(binary)
            # 현재 i 번째에서 만든 코드
            password = []

            # 코드의 맨끝이 1이니까 뒤에서 부터 비율 계산산
            for i in range(l - 1, -1, -1):
                if binary[i] == '1' and ratio[2] == 0:
                    # 마지막 1의 비율 계산중
                    ratio[3] += 1
                elif binary[i] == '0' and ratio[1] == 0:
                    ratio[2] += 1
                elif binary[i] == '1' and ratio[0] == 0:
                    ratio[1] += 1
                elif binary[i] == '0' and binary[i - 1] == '1':
                    # 처음부분 0 만남, 터름부분 0의 비율은 계산 안해도 됨
                    # 나머지 3부분의 비율만 봐도 된다
                    # 여기서 부터 코드 변환 하자
                    min_v = min(ratio[1:4])  # 제일 작은 숫자 찾아서나누기
                    # 숫자 하나
                    number = pat.get((ratio[1] // min_v, ratio[2] // min_v, ratio[3] // min_v))
                    # 숫자 하나 만든거
                    password.append(number)
                    ratio = [0] * 4

                    if len(password) == 8:
                        passcode = password[::-1]
                        odd = passcode[0] + passcode[2] + passcode[4] + passcode[6]
                        even = passcode[1] + passcode[3] + passcode[5] + passcode[7]

                        cal = odd * 3 + even

                        if cal % 10 == 0 and password not in dup_check:
                            total += odd + even

                            dup_check.append(password)

                        password = []

    print(f'#{tc} {total}')
