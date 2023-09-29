'''
1
- 테스트 케이스 받기
    - 무한으로 받고 입력 예외시 브레이크

- (a*b)%c == (a%c*b%c)%c와 같아서
111 % 3 == (11 * 10 + 1) %3 
'''

while True:
    try:
        n = int(input())
    except:
        break
    i = 1
    num = 0

    while True:
        num = num*10 + 1
        num %= n
        if num == 0:
            print(i)
            break
        i += 1