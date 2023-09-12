# 큐
import sys

def push(x):
    q.append(x)
    pass

# 명령의 수
N = int(sys.stdin.readline())
q = []
for _ in range(N):
    command = sys.stdin.readline().split()
    l = len(command)
    if l == 2: # 명령어가 push라면
        push(command[1])

    else: # 아니고 다른거라면
        if command[0] == "pop":
        elif command[0] == "size":
        elif command[0] == "empty":
        elif command[0] == "front":
        elif command[0] == "back":
