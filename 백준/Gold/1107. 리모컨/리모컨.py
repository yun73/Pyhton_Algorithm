'''
리모컨


- 리모컨
    - 버튼 : 0 ~ 9 숫자, + 와 -
    - '+' : 보고있는 채널에서 +1
    - '-' : 보고있는 채널에서 -1
    - 채널 : 무한대
    - 채널 0에서 -를 누른 경우에는 채널이 변하지 않고

- 수빈이가 지금 이동하려고 하는 채널은 N이다
- 어떤 버튼이 고장났는지 주어졌을 때


- 안고장난 버튼으로 주어진 숫자와 가장 가깝게 한번에 이동할수 있다
- + 와 - 버튼은 1 씩만 채널을 변경할 수 있기 떄문에

- 리모컨 누르는 경우의 수
1. 해당 번호가 다 있는경우
    - 버튼을 다 누른게 최소 - 자리수 만큼
    - 채널 +,- 하는게 최소 - 두 숫자 차이만큼
2. 해당 번호가 다 없는 경우
    - 다 눌러보면서 가까운 숫자 찾기
    - 근데 큰숫자 에 채널 - 하는 경우
    - 작은 숫자에 채널 + 하는 경우 두가지
3. 모든 번호가 없는 경우
    - 두 숫자 차이의 절대값 만큼
4. 모든 번호 있는 경우는 해당 번호 있는 경우랑 같음
5.


'''

N = input()
M = int(input())
is_bk_btn =[0]*10
if M != 0:
    btn = list(map(int, input().split()))
    for b in btn:
        is_bk_btn[b] = 1
# 현재 위치
now_ch = '100'
min_click = abs(int(N)-100)

def bt(i,now,N):
    global min_click
    # i 는 10의 지수
    # 리모컨으로 1의 자리부터 입력할 거임
    if (i == len(N)+1 or i == len(N) or i == len(N)-1) and not i == 0:
        if i + abs(now-int(N)) < min_click:
            # print(now)
            # print(i)
            min_click = i + abs(now-int(N))

        if i == len(N)+1:
            return

    # 모든 숫자들 중 안 부서진 숫자들로 다 눌러보기
    for num in range(10):
        # 부서진 버튼이면 건너뛰기
        if is_bk_btn[num]:
            continue
        bt(i+1,now+num*10**i,N)


if now_ch == N:
    print(0)
elif M == 0:
    print(min(len(N),abs(int(N)-100)))
elif M == 10:
    print(abs(int(N)-int(now_ch)))
else:
    bt(0,0,N)
    print(min_click)