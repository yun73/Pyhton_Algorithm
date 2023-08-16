T = 1
isp = {'*' : 2, '+': 1}
icp = {'*' : 2 , '+': 1}

def cal(postfix):
    stack = []
    for c in range(postfix):
        if c not in ['+', '*']:
            stack.append(int(c))
        else:
            right = stack.pop()
            left = stack.pop()
            if c == '*':
                stack.append(left*right)
            elif c == '+':
                stack.append(left+right)

    return stack.pop()


for tc in range(1,T+1):
    N = int(input())
    susik = input()
    postfix = '' # 후위표기식
    op = [] # 연산자 스택
    for c in range(N):
        # 나온 토큰이 숫자이면
        if susik[c] not in ['+', '*']:
            postfix += susik[c]
            if c == N-1:
                while op:
                    postfix += op.pop()
        else: # 연산자가 나오면
            if not op:
                op.append(susik[c])
            else:
                if isp[op[-1]]<icp[susik[c]]: # ** ++ + *
                    op.append(susik[c])
                elif isp[op[-1]]>=icp[susik[c]] : # * +
                    while isp[op[-1]]<icp[susik[c]]:
                        postfix += op.pop()
                    op.append(susik)

    print(postfix)

    result = cal(postfix)
    print(f'#{tc} {result}')

# 9+5*2+3+2
# 952
# +*
# 952*+

