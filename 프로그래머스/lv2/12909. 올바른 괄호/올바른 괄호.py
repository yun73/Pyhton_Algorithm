# 프로그래머스
# 올바른 괄호
def solution(s):
    stack = [0]*100000 # 괄호 스택
    top = -1
    for b in s:
        if b == '(':
            top += 1
            stack[top] = b

        else: # 괄호가 닫는 괄호일 떄
            if top > -1: # .앞에 있는 여는 괄호랑 짝지어서 나가
                top -= 1
            else: #  스택에 아무것도 들어있지 않을 때
                return False
    # 괄호검사 끝나고 나와서
    if top == -1:
        return True
    else:
        return False