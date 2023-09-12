# 큐

import sys

def push(q,X): # q 에 x를 push
    q.append(X)
    return

def pop(q):
    if q: # 들어있는 경우
        return q.pop(0)
    else:
        return -1

def size(q):
    return len(q)

def is_empty(q):
    if q:
        return 0
    else:
        return 1

def front(q):
    if q:
        return q[0]
    else:
        return -1

def back(q):
    if q:
        return q[-1]
    else:
        return -1

N = int(sys.stdin.readline()) # 명령의 개수

q = []
# front와 top 을 이용해서도 구현가능
for _ in range(N):
    command = sys.stdin.readline().split()
    if len(command) == 2: # 2개 입력? -> push 입력 받음
        push(q, command[1])
    else:
        if command[0] == "pop":
            print(pop(q))
        elif command[0] == "size":
            print(size(q))
        elif command[0] == "empty":
            print(is_empty(q))
        elif command[0] == "front":
            print(front(q))
        elif command[0] == "back":
            print(back(q))