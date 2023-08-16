def cal(postfix):

    stack = []

    for c in postfix:
        if c not in ['+', '*']:
            stack.append(int(c))
        else:
            right = stack.pop()
            left = stack.pop()
            if c == '+':
                stack.append(left + right)
            elif c == '*':
                stack.append(left * right)

    return stack.pop()

T = 10
isp = {'+': 1, '*':2}
icp = {'+': 1, '*':2}


for tc in range(1,T+1):
    N = int(input()) # 문자열의 길이
    susik = input()
    postfix = ''
    op = [0]  # 연산자 저장용

    for i in range(N):
        if susik[i] not in ['+', '*']:
            postfix += susik[i]
            if i == N-1:
                while len(op) > 1:
                    postfix += op.pop()

        else: # 연산자가 나오면
            if len(op) == 1: # op 에 아무값도 없으면
                op.append(susik[i])
            else:
                if isp[op[-1]] < isp[susik[i]]:
                    op.append(susik[i])
                else:
                    while len(op) > 1 and isp[op[-1]] >= isp[susik[i]]:
                        postfix += op.pop()
                    op.append(susik[i])
    # print(postfix)
    result = cal(postfix)

    print(f'#{tc} {result}')