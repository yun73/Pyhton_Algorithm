
bit = "0000000111100000011000000111100110000110000111100111100111111001100111"

n = len(bit)

# bin() : 2진수로 바꿔주는 함수
# hex() : 16진수로 바꿔주는 함수

# 0b : 이진수
# 0o : 팔진수
# 0x : 16진수 10 : A, 11 : B
# 0xA == 10

# 파이썬 기능 사용하기
for i in range(0, n, 7):
    bit7 = "0b" + bit[i:i+7]
    dec = int(bit7, 2)
    print(dec, end = ' ')
print()
# 이진수를 7칸씩 쪼개서 십진수로 만들기
for i in range(0, n, 7):
    bit7 = bit[i:i+7]
    # print(bit7)
    base = 2 # 지수 밑
    ex = 6 # 거듭제곱
    dec = 0 # 십진수 값
    for b in bit7:
        dec += int(b) * base**ex
        ex -= 1
    # 만들어진 십진수 출력
    print(dec, end = ' ')
