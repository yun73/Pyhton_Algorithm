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


import sys
word = list(sys.stdin.readline().rstrip())

i = 0
start = 0

while i < len(word):
    if word[i] == "<":       # 열린 괄호를 만나면
        i += 1
        while word[i] != ">":      # 닫힌 괄호를 만날 때 까지
            i += 1
        i += 1               # 닫힌 괄호를 만난 후 인덱스를 하나 증가시킨다
    elif word[i].isalnum(): # 숫자나 알파벳을 만나면
        start = i
        while i < len(word) and word[i].isalnum():
            i+=1
        tmp = word[start:i] # 숫자,알파벳 범위에 있는 것들을
        tmp.reverse()       # 뒤집는다
        word[start:i] = tmp
    else:                   # 괄호도 아니고 알파,숫자도 아닌것 = 공백
        i+=1                # 그냥 증가시킨다

print("".join(word))