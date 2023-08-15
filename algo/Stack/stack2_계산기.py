# 중위표기법 -  연산자를 피연산자의 가운데 표기
# 후위표기법 - 연산자를 피연산자 뒤에 표기하는 방법
# 후위 표기법은 괄호의 위치 ㅣㄴ경 안쓰고 해결 가능
# step1 중위표기식 > 후위표기식
# 각 연산자들이 stack 내부에 있을 때랑 외부에 있을 때랑 우선순위를 다르게 해서
# ( 는 스택 외부에서 가장 우선순위 크게하여 스택에 집어넣고
# 스택 내부에서 젤 아래로 하여 나오지 않도록 한다
'''
(6+5*(2-8)/2)
'''
stack = [0] * 100
top = -1
icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}

fx = '(6+5*(2-8)/2)'
susik = ''

for x in fx:
    if x not in '(+-*/)':
        susik += x
    elif x == ')': #'(' 까지 pop
        while stack[top] != '(': #peek
            susik += stack[top]
            top -= 1

        top -= 1  # '(' 버림 pop
    else:
        if top == -1 or isp[stack[top]] < icp[x]: # 들어오려는 토크의 우선순위가 높으면
            top += 1 # push
            stack[top] = x
        elif isp[stack[top]] >= icp[x]:
            while top > -1 and isp[stack[top]] >= icp[x]:
                susik += stack[top]
                top -= 1
                top += 1
                stack[top]

# step2 후위표기식 > 중위표기식 계산
# 피연산자 계속 푸쉬 연산자 나오면 앞의 두개 피연산자 가져와서 계산후 그 값을 푸슈ㅣ

'''
6526-*2/+
'''

stack = [0] * 100
top = -1
susik = '6528-*2/+'
for x in susik:
    # 피연산자이면
    if x not in '+-/*':
        top += 1
        stack[top] = int(x)
    else:
        op1 = stack[top]
        top -= 1
        op2 = stack[top]
        top -= 1
        if x == '+':  # op2 + op1 >> 밸셈, 나눗셈의 경우 뺴내는 순서를 고려
            top += 1
            stack[top] = op2 + op1
        elif x == '-':
            top += 1
            stack[top] = op2 - op1
        elif x == '/':
            top += 1
            stack[top] = op2 / op1
        elif x == '*':
            top += 1
            stack[top] = op2 * op1

print(stack[top])



