# 스택 수열
# LIFO
# push 는  +
# pop 은  -
import sys

n = int(sys.stdin.readline())
# 찾아야할 수열의 첫 숫자
before = 1
# 숫자 저장
stack = []
# 스택 연산 저장
re = ''
for _ in range(n):
    # 찾아야할 숫자
    num = int(sys.stdin.readline())
    # pop 할 때 뒤에 나올 숫자를 빼버리면 안됨
    # if num in stack: 이거 때문에 시간 초과 나는듯
    # 찾아야할 숫자이하에서 나올 때까지
    if num >= before:
        for i in range(before, num + 1):
            stack.append(i)
            re += '+\n'
        # n개의 숫자를 넣으면서 마지막에 넣은 갑
        before = num + 1
        # 찾은 숫자 꺼내서 수열 만들기
        stack.pop()
        re += '-\n'
    else:
        # 스택의 맨ㅇ
        if stack[-1] != num:
            re = "NO"
            break # for
        else:
            stack.pop()
            re += '-\n'

print(re)