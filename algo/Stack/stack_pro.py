# 괄호 검사
# 왼쪽 오른쪽 괄호의 개수가 같아야 함
# 같은 괄호에서 왼쪽 괄호는 오른쪽보다 먼저 나와야 함
# 괄호 사이에는 포함관계만 존재

# 1. 수식 끝, 괄호 남음 isempty()> False`
# 2. 닫는괄호. 스택이 비어있어
T = int(input())
for tc in range(1, T+1):
    row = input() # 괄호의 짝이 맞는지 검사할 문자열
    stack = [] # 스택, 만약 미리 지정시 최대 삽입 횟수만큼
    # bracket = [] # 오류난 닫는 괄호 저장
    answer = 1 # 1이면 괄호가 제대로 되어있다, 0이면 제대로 xx

    # 괄호검사
    # row에서 한글자씩 가져와서 검사
    # 가져온 글자가 만약 여는 괄호면 스택에 삽입
    # 뗴어낸 글자가 닫는 괄호면 => 스택에서 하나 꺼내고
    # 짝이 맞는지 검사
    # 꺼내오기 전에 스택이 비어있나 확인, 비어있으면 오류
    for b in row:
        if b == '(':
            stack.append(b)
            # print(f'#{tc} {stack}')

        elif b == ')':
            if len(stack) == 0:
                answer = 0
                # bracket.append(b)
                break

            c = stack.pop()
            if not(c == '(' and b == ')'):
                answer = 0
                break
            # print(f'#{tc} {stack}')
        else:
            continue

    # print(f'#{tc} {stack}')
    # print(f'#{tc} bracket : {bracket}')

    # 모든 글자 검사 끝난 후에 스택 비어 있지 않으면 오류
    if len(stack) > 0:
        answer = 0

    print(f'#{tc} {answer}')

'''
4
( )( )((( )))
((( )((((( )( )((( )( ))((( ))))))
())
(()
'''

#
# # function call 함수호출 동작 원리 잘 이해해야지 > 나중에 재귀함수
# # 프로그램에서의 함수 호출과 복귀에 따른 수행 순서를 관리
#
# # 재귀 호출
# # 자기 자신을 호출하여 순환
# # 반복문 처럼 생각 X, 다른 함수 호ㅜㄹ하는 것 처럼 생각
# # 피보나치 수열 만들어보기 >> 문제점 엄청난 중복 호출 존재
# def fibo(n):
#     if n < 2:
#         return n
#     else:
#         return fibo(n - 1) + fibo(n - 2)
#
#
# print(fibo(8))
#
#
# # 메모이제이션(memoization) 동적계획법(DP)의 핵심 기술
# # 이전에 계산한 값을 저장해서 다시 계산하지 안홁 해서 전체적인 실행속도 빠르게
# def fibo1(n):
#     global memo
#     if n >= 2 and memo[n] == 0:
#         memo[n] = (fibo1(n - 1) + fibo1(n - 2))
#     return memo[n]
#
# n = 8
# memo = [0] * (n + 1)
# memo[0] = 0
# memo[1] = 1
# print(fibo1(n))
