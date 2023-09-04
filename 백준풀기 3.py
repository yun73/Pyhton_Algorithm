# 스택
# 정수를 저장하는 스택 구현
import sys
input = sys.stdin.readline

# 명령의 수
N = int(input())
stack = [0]*10000
top = -1
for i in range(N):
    command = input()
    if 'push' in command:
        push, num = command.split(' ')
        print(push, num)
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

T = int(input())
for tc in range(T):
    N = int(input())

    answer = 0

    answer_l = []

    count = 0

    for i in range(1, N+1):
        if i == 1:
            answer = 0
            answer_l.append(1)
        if i == 2:
            answer = 1
            answer_l.append(2)
        if i == 3:
            answer = 3
            answer_l.append(4)
        if i >= 4:
            count = sum(answer_l)
            answer = count
            answer_l.append(count)
            answer_l.pop(0)

    print(answer)