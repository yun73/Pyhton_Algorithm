
N = int(input()) # 계단의 개수
floor = [0] * (N+1)
for f in range(1,N+1):
    floor[f] = int(input())

n = N # 도착점의 인덱스

point = floor[n]
step = [] # 내려간 계단 수

while n > 1: # n이 아무 값도 없는 인덱스에 도착하면 종료
    if floor[n-1] >= (floor[n-2] + floor[n])/2:

        if step[-1] == 1: # 스텝의 마지막 값이 1이면
            step.append(2)
            point += floor[n - 2]
            n -= 2

        else:
            step.append(1)
            point += floor[n-1]
            n -= 1
    else:
        if n == 2:
            if step[-1] != 1:
                step.append(1)
                point += floor[n - 1]
                n -= 1
        else:
            step.append(2)
            point += floor[n-2]
            n -= 2

print(point)




