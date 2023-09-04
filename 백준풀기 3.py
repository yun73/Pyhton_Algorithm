# 스택
# 정수를 저장하는 스택 구현

# 명령의 수
N = int(input())
stack = [0]*10000
top = -1
for i in range(N):
    command = input()
    if 'push' in command:
        push, num = command.split(' ')
        top += 1
        stack[top] = int(num)
    elif command == 'top':
        if top == -1:
            print(-1)
        else:
            print(stack[top])
    elif command == 'size':
        if top == -1:
            print(0)
        else:
            print(top+1)
    elif command == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    elif command == 'pop':
        if top == -1:
            print(-1)
        else:
            print(stack[top])
            top -= 1