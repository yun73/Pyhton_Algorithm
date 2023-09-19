'''
1일 이용권
1달 이용권 : 매달 1일부터
3달 이용권 : 연속 3달 , 매달 1일부터, 11,12월에도 사용가능
다음 해의 이용권만을 구매할 수 있기 때문에 3달 이용권은 11월, 12월, 1윌 이나 12월, 1월, 2월 동안 사용하도록 구매할 수는 없다.)
1년 이용권 : 매년 1월 1일부터
'''
def bt(r,total,dm):
    global min_total

    if r >= 12:
        if min_total > total:
            min_total = total
        return
    else:
        if plan[r]:
            bt(r+1,total+dm[r],dm)
            # 3달
            bt(r + 3, total + month_3,dm)

        else:
            bt(r + 1, total,dm)

T = int(input())
for tc in range(1,T+1):
    # 1일 1달 3달 1년 이용권 가격
    day,month,month_3,year = map(int, input().split())
    # 이용계획
    plan = list(map(int, input().split()))

    visited = [0]*12
    dm = [0]*12
    for i in range(12):
        if plan[i]:
            dm[i]=min(plan[i] * day , month)

    # 연간 이용권을 min 값으로
    min_total = year
    
    bt(0,0,dm)

    print(f'#{tc} {min_total}')
