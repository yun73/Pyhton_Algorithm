import sys
input = sys.stdin.readline

n = int(input())
stack = []
before = 1
res = ''
for _ in range(n):
    num = int(input()) # 찾을 숫자
    if num >= before:
        for i in range(before, num + 1):
            stack.append(i)
            res += '+\n'

        before = num + 1 # 마지막에 넣은 값
        stack.pop() # 찾은 숫자 빼기
        res += '-\n'
    else:
        if stack[-1] != num:
            res = "NO"
            break
        else:
            stack.pop()
            res += '-\n'

print(res)