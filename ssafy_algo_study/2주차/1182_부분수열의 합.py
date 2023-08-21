
# r번 째 숫자부터 N번 째 숫자 까지 숫자를 골라 부분집합을 만들고
# 해당 부분수열의 합인 S 가 구하고자하는 합과 같으면 개수 세주자
def sumsub(r, N, S, nowsum):
    global cnt
    global num
    # 만약 r이 N에 도달하면 부분집합 하나 만들어진거
    if r == N:
        if nowsum == S:
            cnt += 1
            return
    else:
        if check[r] == 0:
            check[r] = 1
            sumsub(r + 1, N, S, nowsum + num[r])
            check[r] = 0
            sumsub(r + 1, N, S, nowsum)


N, S = map(int,input().split())
num = list(map(int, input().split()))
check = [0] * N
cnt = 0
sumsub(0, N, S, 0)
if S == 0:
    print(cnt-1) # 공집합 제외
else:
    print(cnt)
'''
5 5
-7 -3 -2 5 8
'''