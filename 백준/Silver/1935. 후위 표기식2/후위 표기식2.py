# 후위 표기식
# 피연산자의 개수
N = int(input())
# 수식
susik = input()
# 숫자 저장할 딕셔너리
alpha = {}
num = []
for c in susik:
    # 피연산자가 나왔을 때 숫자를 입력받아 저장하자
    if c not in ['*', '+', '-', '/']:
        # 아직 입력받지 않은 피연산자라면 입력받아서 추가
        if c not in alpha.keys():
            alpha[c] = int(input())
        num.append(alpha[c])
    else: # 연산자가 나오면 숫자 2개 꺼내서 게산하자
        # '-', '/' 같은 경우 순서에 주의
        right = num.pop()
        left = num.pop()
        if c == '+':
            # 계산한 숫자를 다시 숫자 스택에 추가 다음계산 해야함
            num.append(left+right)
        elif c == '-':
            num.append(left-right)
        elif c == '*':
            num.append(left*right)
        elif c == '/':
            num.append(left/right)

# 숫자 스택에 마지막에 하나만 남아있을 거임
print(f'{num[0]:.2f}')