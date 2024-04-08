import sys
input = sys.stdin.readline

n = int(input())
stack = []
before = 1
res = []
for _ in range(n):
    num = int(input()) # 찾을 숫자

    while before <= num:
        stack.append(before)
        res.append('+')
        before += 1  # 마지막에 넣은 값


    if stack[-1] != num:
        res=["NO"]
        break
    else:
        stack.pop()
        res.append('-')

print('\n'.join(res))