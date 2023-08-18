T = int(input())

# 암호 문자열
password = list(map(int, input().split()))

# 암호의 길이
N = 8

# 큐 생성(원형 큐)
q = [0] * (N+1)
front = rear = 0

# 처음 n번 큐에 넣기
for i in range(N):
    rear = (rear+1)%N
    q[rear] = [rear+1]%N
    q[rear] = password[i]

    # 빼줄 숫자
    number = 1

    while True:
        # 비밀번호 하나 꺼내서
        # number을 빼준 후에 다시 큐에 넣기
        front = (front+1) % N
        item = q[front]

        # 숫자 빼와서 감소 시켰는데
        # 만약 0 이하가 되어버렸다
        # 숫자를 0으로 바꾸ㅡ고 큐의 맨 뒤에 넣은 다음 종료
