T = 10
for tc in range(1, T + 1):
    N, code = input().split()

    password = []
    password.append(code[0])

    for i in range(1,int(N)):
        if len(password) < 1:
            password.append(code[i])
        else:
            if password[-1] == code[i]:
                password.pop()
            else:
                password.append(code[i])

    result = "".join(password)

    print(f'#{tc} {result}')

# T = 10
# for tc in range(1, T + 1):
#     N, code = input().split()
#
#     password = []
#     password.append(code[0])
#
#     for i in range(1, int(N)):
#         if len(password) > 0:
#             num = password.pop()
#             if num != code[i]:
#                 password.append(num)
#                 password.append(code[i])
#         else:
#             password.append(code[i])
#
#     result = "".join(password)
#
#     print(f'#{tc} {result}')`
