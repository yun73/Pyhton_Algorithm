T = int(input())
for tc in range(1, T + 1):
    code = input()  # 주어진 입력

    # 하나씩 저장하며 확인할 스택
    stack = [0]*100

    # 정상적으로 짝 1, 비정상 0
    answer = 1
    top = -1
    for c in code:

        if c == '(' or c == '{':
            top += 1
            stack[top] = c

        elif c == ')' or c == '}':
            if top == -1:
                answer = 0
                break
            top -= 1
            b = stack[top+1]
            if (b != '(' and c == ')') or (b != '{' and c == '}'):
                answer = 0
                break

        else:
            continue

    if top != -1:
        answer = 0

    print(f'#{tc} {answer}')

#  # ==============pop, append 안쓰고 해보기
# T = int(input())
# for tc in range(1, T + 1):
#     code = input()  # 주어진 입력
#
#     # 하나씩 저장하며 확인할 스택
#     stack = []
#
#     # 정상적으로 짝 1, 비정상 0
#     answer = 1
#
#     for c in code:
#
#         if c == '(' or c == '{':
#             stack.append(c)
#
#         elif c == ')' or c == '}':
#             if len(stack) == 0:
#                 answer = 0
#                 break
#
#             b = stack.pop()
#             if (b != '(' and c == ')') or (b != '{' and c == '}'):
#                 answer = 0
#                 break
#
#         else:
#             continue
#
#     if len(stack) > 0:
#         answer = 0
#
#     print(f'#{tc} {answer}')
