# 후위표기식으로 바꾸기
def get_postfix(susik):
    postfix = ''
    stack = []

    for c in susik:
        if c != '+':  # 숫자가 나오면 push
            postfix += c
            if stack:
                postfix += stack.pop()
        else: # 연산자 나오면
            stack.append(c)

    # 남아있는 연산자 붙여주고 끝
    if stack:
        postfix += stack.pop()

    return postfix

# 바꾼 후위표기식 계산하기
def get_result(postfix):

    stack = []
    for c in postfix:
        if c != '+':  # 숫자면 스택에 저장
            stack.append(int(c))
        else:  # 연산자 나오면 stack에서 두개의 숫자 꺼내서 연산하기

            right = stack.pop()
            left = stack.pop()
            result = left + right
            # 스택에 다음 연산을 위해 결과 저장
            stack.append(result)

    return stack.pop()


T = 10
for tc in range(1,T+1):
    n = int(input()) #문자열의 길이
    susik = input()

    postfix = get_postfix(susik)
    # print(postfix)
    result = get_result(postfix)

    print(f'#{tc} {result}')