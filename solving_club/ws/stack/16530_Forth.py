def get_result(susik):
    stack = []

    for c in susik: # 주어진 수식에서 하나씩 꺼내기
        # 만약 숫자이면 피연산자이면
        if c not in '+*-/.':
            # 스택에 추가
            stack.append(int(c))
        elif c == '.': # c 가 점이면 숫자 반환
            if len(stack) > 1:
                return 'error'
            else:
                return stack.pop()

        else: # 만약 c가 연산자이면 연산할 숫자 두개 꺼내기
            # 근데 만약 스택에 남은 숫자가 하나라면 error 출력
            if len(stack) < 2:
                return 'error'

            else:
                right = stack.pop()
                left = stack.pop()
                if c == '+':
                    result = left + right
                elif c == '-':
                    result = left - right
                elif c == '*':
                    result = left * right
                elif c == '/':
                    result = left // right
                # 연산결과 또 사용해야함
                stack.append(result)



T = int(input())
for tc in range(1, T+1):
    susik = list(input().split())

    print(f'#{tc} {get_result(susik)}')