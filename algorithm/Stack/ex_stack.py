stack = [0] * 10
top = -1

top += 1            # push(1)
stack[top] = 1
top += 1            # push(2)
stack[top] = 2
top += 1            # push(3)
stack[top] = 3
top += 1            # push(4)
stack[top] = 4

print(stack[top])   # pop()
top -= 1
top -= 1            # pop()
print(stack[top+1])

# 스택 사용(파이썬)
stack = []

def py_push(item):
    stack.append(item)

def py_pop():
    if len(stack) == 0:
        # 언더플로우!
        return
    else:
        return stack.pop()

for i in range(10):
    py_push(i)

print(stack)

for i in range(10):
    print(py_pop(), end= ' ')

print()
print(stack)

top = -1 # 원소를 마지막으로 삽입한 위치
size = 10
stack = [0] * size

def my_push(item):
    global top
    top += 1
    if top == size:
        # overflow
        print('overflow')
    else:
        stack[top] = item

def my_pop(): # 이렇게 할경우 데이터를 삭제하는게 아니라 인덱스를 조작
    global top
    if top == -1:
        print('underflow')
        return
    else:
        top -= 1
        return stack[top+1]

def peek():
    # top -1 이면 원소가 없다.
    if top > -1:
        return stack[top]

for i in range(10):
    my_push(i)

print(stack, top)

for i in range(10):
    print(my_pop(), end= ' ')

print()
print(stack, top)

my_push(100)

print(stack, top)



