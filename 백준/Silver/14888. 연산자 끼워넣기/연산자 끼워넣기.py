# 연산자 끼워넣기
# N 개의 수로 이루어진 수열 A
# N-1 개의 연산자
# +-x/
# 수의 순서를 바꾸지 말고 연산자를 넣어서
# 식의 계산은 연산자 순위 무시하고 앞에서부터 진행
# / = //
# 음수를 양수로 나눌때는 양수로 바꾼뒤 몫 얻은 다음 몫의 부호 반대로
# 최대 겨로가와 최소결과

# A : 숫자 리스트
# op : 연산자 리스트
# cal : 지금까지의 계산 결과
def bt(r,N,A,op,cal):
    global max_cal
    global min_cal

    # 종료조건
    if r == N-1: # 모든 수를 다 사용하면

        if max_cal < cal:
            max_cal = cal
        if min_cal> cal:
            min_cal = cal
        return
    else:
        # op에 들어있는 연산자를 하나씩 꺼내서 쓸거야
        for i in range(4):
            if op[i]: # 만약 해당 연산자가 존재하면
                # 하나 사용하고
                op[i] -= 1
                # 다음 연산하러 가는데
                # 무조건 앞에서부터 계산하고
                # 음수나눗셈일 때만 계산을 다르게 하자
                if i == 0:
                    bt(r+1,N,A,op,cal + A[r+1])
                elif i == 1:
                    bt(r + 1, N, A, op, cal - A[r + 1])
                elif i == 2:
                    bt(r + 1, N, A, op, cal * A[r + 1])
                elif i ==3:
                    if cal >= 0:
                        bt(r + 1, N, A, op, cal// A[r + 1])
                    else:
                        bt(r + 1, N, A, op, -(abs(cal) // A[r + 1]))

                # 갔다와서 사용안했다고 하고 다른 경우도 보러 가자
                op[i] += 1

# 수의 개수
N = int(input())
# 숫자 리스트
A = list(map(int, input().split()))
# 합이 N-1인 4개의 정수
# 앞에서 부터  + - x // 의 개수
op = list(map(int, input().split()))
max_cal = -10**9 - 1
min_cal = 10**9 + 1
bt(0,N,A,op,A[0])

print(max_cal)
print(min_cal)