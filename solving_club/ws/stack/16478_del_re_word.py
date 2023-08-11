T = 10
for tc in range(1, T + 1):
    text = input()

    stack = []

    for word in text:
        if len(stack) < 1:
            stack.append(word)

        else:
            if stack[-1] == word:
                stack.pop()
                continue
            else:
                stack.append(word)

    result = len(stack)

    print(f'#{tc} {result}')

# T = int(input())
# for tc in range(1, T + 1):
#     text = input()
#
#     size = 1000
#     stack = [0] * size
#     top = -1
#
#     # 스택을 이용해서 풀건데
#     # 일단 문자를 스택에 넣어 (맨 처음 글자는 넣음)
#     top += 1
#     stack[top] = text[0]
#     # 두번째 글자부터는 내가 제일 최근에 넣었던 글자와 비교해서
#     for i in range(1,len(text)):
#         # 만약 같다면 스택에서 pop
#         if top != -1 and stack[top] == text[i]:
#             top = -1
#         # 다르다면 현재글자를 스택에 push
#         else:
#             top += 1
#             stack[top] = text[i]
#
# print(f'#{tc} {top+1}')

