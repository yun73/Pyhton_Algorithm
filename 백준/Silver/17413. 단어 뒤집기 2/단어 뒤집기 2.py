# 단어 뒤집기
# 문자열 S 단어만 뒤집기
# 단어 사이 공백
# <> 안에는 부분 문자열 안뒤집어

S = input()
# 부분 단어 판단
result = ''
i = 0
while i < len(S):
    stack = '' # 한 덩어리
    # 여는 괄호 나오면
    if S[i] == '<':
        while True:
            if S[i] == '>':
                result += S[i]
                i += 1
                break
            # 닫는 괄호 나올 때까지
            result += S[i]
            i += 1

    else: # 아닐 경우엔
        while True:
            if i == len(S)-1:
                stack = S[i] + stack
                result += stack
                i += 1
                break
            if S[i] == ' ':# 공백 나올 때까지
                stack += S[i]
                result += stack
                i += 1
                break
            if S[i] == '<':
                result += stack
                break

            stack = S[i] + stack
            i += 1

print(result)