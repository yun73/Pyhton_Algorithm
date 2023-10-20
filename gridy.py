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
-
- + 와 - 버튼은 1 씩만 채널을 변경할 수 있기 떄문에
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
min_click = int(1e9)
# 주어진 숫자랑 현재 채널 위치랑 같아질 때까지 진행행
# 해당 숫자가 없으면 가장 가까운 숫자로 해야하는데
# 각 위치 확일 할 때 그 시점의 최소값이 전체의 최소값으로 만들어줄지는 모름
# 같은 자리 문자열을 만들고 결과값 숫자로 바꿔서 비교
# 최소값 저장
def bt(i,end,now,now_click):
    global min_click
    # 종료 조건
    if i == end:
        print(end)
        click = i + abs((len(N) - len(str(int(now)))))
        result = abs(int(N) - int(now)) + click
        min_click = min(min_click, result)
        return


    # 만약 만들어야 하는 숫자가 안부서졌으면
    # 부서졌으면 안부서진거 중에 클릭
    for num in range(10):
        if is_bk_btn[num]:
            continue
        bt(i+1,end,str(num)+now,)


if now_ch == N:
    print(0)
elif M == 0:
    print(min(len(N),abs(int(N)-100)))
elif M == 10:
    print(abs(int(N)-int(now_ch)))
else:
    bt(0,len(N)+1,'',0)
    print(min_click)