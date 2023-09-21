pat = {
    "001101": 0,
    "010011": 1,
    "111011": 2,
    "110001": 3,
    "100011": 4,
    "110111": 5,
    "001011": 6,
    "111101": 7,
    "011001": 8,
    "101111": 9,
}



hex1= "0DEC"
hex2= "0269FAC9A0"

def find_pattern(hex_string):
    # hex_string 은 16진수 문자열
    # 이진수 문자열로 바꾸면 길이가 4배
    l = len(hex_string) * 4
    x = int(hex_string, 16) # 숫자로 바꾸기

    # 숫자를 다시 이진수 문자열로 바꾸자
    bin_string = ""

    # i 번째 비트를 검사해서 겨로가가 0 => i 번째 비트는 0
    # 결과가 0이 아니면 i번째 비트는 1
    for i in range(l-1,-1,-1):
        if x & (1<<i):
            bin_string += '1'
        else:
            bin_string += '0'




    password = []
    # 뒤에서부터 검사해서 1을 만나면 암호해독 시작
    # 1을 만난 순간부터 6개씩 잘라서 검사
    for i in range(l-1,-1,-1):
        if bin_string[i] == '1': # 1만나면
            j = i
            while True:
                if bin_string[j] == '1':  # 1만나면
                    # 암호해독하고
                    # 다음 패턴 찾으러 6만큼 앞으로
                    if bin_string[j-5:j+1] in pat.keys():
                        password.append(pat[bin_string[j-5:j+1]])
                        password.append(pat.get(bin_string[j-5:j+1]))
                    j -= 6
                else:
                    break
        if password:
            break

    print(*password[::-1])

find_pattern(hex1)
find_pattern(hex2)