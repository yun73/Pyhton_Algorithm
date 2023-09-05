# 스택
# 정수를 저장하는 스택 구현
import sys

# 명령의 수
N = int(sys.stdin.readline())
stack = [0]*10000
top = -1
for i in range(N):
    command = sys.stdin.readline().rstrip()
    if 'push' in command:
        push, num = command.split(' ')
        top += 1
        stack[top] = int(num)
    elif 'top' in command:
        if top == -1:
            print(-1)
        else:
            print(stack[top])
    elif 'size' in command:
        if top == -1:
            print(0)
        else:
            print(top+1)
    elif 'empty' in command :
        if top == -1:
            print(1)
        else:
            print(0)
    elif 'pop' in command :
        if top == -1:
            print(-1)
        else:
            print(stack[top])
            top -= 1
