# 빈 스택에 원소를 차례로 삽입 후 삭제하는 연산 과정
# 후입선출
# 위에 쌓임 젤 위에거가 top
# push 알고리즘 append 메소드를 통해 데이터 삽입
# 비어있는 지 확인
def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow!') # 디버깅을 위한 ㅂ분
    else:
        stack[top] = item

size = 10
stack = [0]*size
top = -1

push(10,size)
top += 1  # push(20)
stack[top] = 20 #

# 스택의 pop 알고리즘
def pop() :
    if len(s) == 0:
        # underflow
        return
    else:
        return s.pop()

def pop():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        top -= 1  # 탑 하나 감소시키고
        return stack[top + 1] # 원래 탑 값 꺼내오기

print(pop())

if top> -1:  # pop()
    top -= 1
    print(stack[top+1])

stack = [1,2]
