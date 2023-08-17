# front와 rear 이용해서 값을 옮기지 말고 인덱스만 옮기자
def enq():
    global rear
    global front
    if (rear + 1) % Qsize == front:
        # front = (front+1)%cQsize # 이경우에는 그냥 밀고 새로운 값 넣어줘
        print('Q is Full')
    else:
        rear = (rear + 1) % Qsize
        # Q[rear] = data
        return rear

def deq():
    global rear
    global front
    if rear == front:
        print('is Empty')
    else:
        front = (front + 1) % Qsize
        # Q[front]
        return front

def rotation(Q, M):
    i = 0
    while i < M:
        # 가장 앞의 숫자 먼저 뺀다 치고 front 옮겨줘
        f = deq()
        # front 증가 시키고 맨 뒤칸인 rear 을 바꿔줘
        r = enq()
        i += 1
    # M번 작업 하고 나서의 front 에 해당하는 값 알려줘
    return Q[front]


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Q = list(map(int, input().split()))
    front = 0
    rear = N - 1
    Qsize = N

    result = rotation(Q, M)

    print(f'#{tc} {result}')