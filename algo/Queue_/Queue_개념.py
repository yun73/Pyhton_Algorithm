'''
- 선입선출 구조
- front : 머리부분 또는 삭제된 위치
- rear :꼬리부분 마지막 삽입 위치
- enQueue, deQueue : 삽입, 삭제
'''
'''
선형큐
- 1차원 배열을 이용한 큐
    - 큐의 크기 = 배열의 크기
    - front : 저장된 첫번째 원소의 인덱스
    - rear  : 정장된 마지막 원소의 인덱스

- 상태표현
    - 초기 상태 : front = rear = -1
    - 공백 상태 : front == rear
    - 포화 상태 : rear == n-1 (n 배열의 크기, n-1 마지막 인덱스)
'''
# 삽입
# 마지막 원소 뒤에 새로운 원소를 삽입하기 위해
# rear 값을 하나 증가시켜 새로운 원소를 삽입할 자리 마련
# 그 인덱스에 해당한ㄴ 배열원소 Q[rear] 에 item을 저장
def enQueue(item):
    global rear
    if rear == Qsize -1: # isFull()
        print('Queue_Full')
    else:
        rear += 1
        Q[rear] = item
        # Queue_.append(a)
# 삭제
# 가장 앞에 있는 원소를 삭제하기 위해
# front 값을 하나 증가시켜 큐에 남아있게 될 첫번째 원소로 이동
# 새로운 첫 번째 원소를 리턴함으로써 삭제와 동일한 기능
def deQueue():
    global front
    if front == rear:
        print('Queue_Empty')
    else:
        front += 1
        return Q[front]
        #return Queue_.pop(0)

def isEmpty():
    return front == rear

def Full():
    return rear == len(Q) - 1

# 검색
# 가장 앞에 있는 원소를 검색하여 반환
# 현재 front의 한자리 뒤에 있는 원소, 즉 큐의 첫 번째에 있는 원소
def Qpeek():
    if isEmpty():
        print('Queue_Empty')
    else:
        return Q[front+1]

'''
- 잘못된 포화상태 인식
    - 선형 큐 이용시 원소 삽입 삭제 계속하면, 배열 앞부분 활용할 수 있음에도
    rear = n-1 인상태로, 포화상태로 인식하여 더 이상의 삽입 못함
    
- 해결방법1
    - 매연산시 원소들을 배열의 앞부분으로 모두 이동시킨다
    - 원소이동에 많은 시간 소요되어 효율성 급격히 떨어짐

- 해결방법2- 원형큐
    - 1차원 배열 사용하되, 논리적으로 배열의 처음과 끝이 연결되어 원형 형태의 큐를 이용
    - front = rear = 0
    - front와 rear의 위치가 n-1을 가리킨 후 처음 인덱스인 0으로 이동해야함
    - 이를 위해 나머지 연산자 mod 이용함
    - front 변수: 공백, 포화 구분 쉽게 하기위해 front 자리 사용 안하고 항상 빈자리
    - 삽입 위치 : rear = (rear + 1) mod n
    - 삭제 위치 ; front = (front + 1) mod n
    - (rear + 1) % len(Q) == front => 포화 상태
'''

Qsize = 3
Q = [0] * Qsize
rear = front = -1

enQueue(1)
enQueue(20)
rear += 1
Q[rear] = 3

while front != rear:
    front += 1
    print(Q[front])


Q.append(1)
Q.append(2)
Q.append(3)
Q.pop(0)
Q.pop(0)
Q.pop(0)

