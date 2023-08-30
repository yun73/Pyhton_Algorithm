def solution(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력


def check_b(binary, b):

    result = int(binary,2) ^ b
    temp = str(bin(result))
    cnt = 0
    for i in range(len(temp)):
        if temp[i] == '1':
            cnt += 1
    if cnt != 1:
        return False
    else:
        return True

def check_t(ternary, t):
    new = solution(t,3)
    if len(new) == len(ternary):
        cnt = 0
        for i in range(len(new)):
            if new[i] != ternary[i]:
                cnt +=1
    else:
        l = abs(len(new) - len(ternary))
        cnt = abs(len(new) - len(ternary))
        if len(new) < len(ternary):
            for i in range(l,len(ternary)):
                if new[i-l] != ternary[i]:
                    cnt += 1
        elif len(new) > len(ternary):
            for i in range(l,len(new)):
                if new[i] != ternary[i-l]:
                    cnt += 1

    if cnt == 1:
        return True
    else:
        return False


T = int(input())
for tc in range(1, T+1):
    binary = input()
    ternary = input()

    sub = abs(int(binary,2) - int(ternary,3))
    remit = 0

    # 잘못된 두 수의 차를 2와 3의 합으로 나타냈을때
    for i in range(0,sub,2):
        # i 는 2의 배수
        other = sub - i
        # 2의 배수만큼 뺐을 때 3으로 나누어 떨어지면
        if other%3==0:
            if int(binary,2) > int(ternary,3):
                b = int(binary,2) - i
                t = int(ternary,3) + other
                if check_t(ternary,t) and check_b(binary,b) and b == t:
                    # 송금액 찾음
                    remit = b
            elif int(binary,2) < int(ternary,3):
                b = int(binary, 2) + i
                t = int(ternary, 3) - other
                if check_t(ternary,t) and check_b(binary,b) and b == t:
                    # 송금액 찾음
                    remit = b


    print(f'#{tc} {remit}')