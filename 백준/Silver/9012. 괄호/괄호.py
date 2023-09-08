# 괄호
# 괄호 검사
import sys

def is_VPS(ps):
    # 괄호를 저장할 스택 생성
    stack = []
    if ps[0] == ')':
        return "NO"
    else:
        stack.append(ps[0])

    for i in range(1,len(ps)-1):
        # 여는 괄호 무조건 넣어주자 근데 만약 닫는 괄호이면 NO 반환
        if ps[i] == "(":
            stack.append(ps[i])
        # 닫는 괄호 나오면 바로 앞에 여는 괄호 인지 확인
        else:
            if stack:
                before = stack.pop()
                if before == "(":
                    # 맞으면 짝지어서 VPS 하나 생성
                    continue
                else:
                     # 틀리면 NO 반환
                    return "NO"
            else:
                return "NO"
    else: # 반복문 다 돌았을 때
        if stack:
            return "NO"
        else:
            return "YES"

T = int (sys.stdin.readline())
for tc in range(1, T+1):
    # 괄호 문자열
    PS = sys.stdin.readline()
    # 괄호 검사
    print(is_VPS(PS))

# readline 쓰면 "input/n" 형식으로 들어옴