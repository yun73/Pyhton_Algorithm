def enq(data):
    global rear
    global front
    if (rear + 1) % cQsize == front:
        # front = (front+1)%cQsize # 이경우에는 그냥 밀고 새로운 값 넣어줘
        print('cQ is Full')
    else:
        rear = (rear + 1) % cQsize
        cQ[rear] = data


def deq():
    global front
    if rear == front:
        print('is Empty')
    else:
        front = (front + 1) % cQsize
        return cQ[front]

cQsize = 4
cQ = [0] * cQsize
front = 0
rear = 0

enq(1)
enq(2)
enq(3)
print(deq())
print(deq())
enq(4)