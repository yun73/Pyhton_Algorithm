# 수영장
# 1년 동안 각 달의 이용 계획 수립
# 가장 적은 비용으로 수영장 이용할 수 있는 방법

'''
1일 이용권
1달 이용권 : 매달 1일부터
3달 이용권 : 연속 3달 , 매달 1일부터, 11,12월에도 사용가능
다음 해의 이용권만을 구매할 수 있기 때문에 3달 이용권은 11월, 12월, 1윌 이나 12월, 1월, 2월 동안 사용하도록 구매할 수는 없다.)
1년 이용권 : 매년 1월 1일부터
'''
def bt(r,total):
    global min_total
    global visited

    if r == 12:
        if min_total > total:
            min_total = total
        return
    else:
        if visited[r] == 0:
            if plan[r]:
                visited[r] = 1
                # 1일
                bt(r+1,total + day*plan[r])
                visited[r] = 0

                # 1달
                visited[r] = 1
                bt(r+1, total + month)
                visited[r] = 0
                # 3달
                if r <= 9:
                    visited[r+1] = 1
                    visited[r+2] = 1
                    bt(r+1,total + month_3)
                    visited[r + 1] = 0
                    visited[r + 2] = 0
                elif r == 10:
                    visited[r+1] = 1
                    bt(r + 1, total + month_3)
                    visited[r + 1] = 1
                else:
                    visited[r] = 1
                    bt(r + 1, total + month_3)
                    visited[r] = 0
            else:
                bt(r + 1, total)



T = int(input())
for tc in range(1,T+1):
    # 1일 1달 3달 1년 이용권 가격
    day,month,month_3,year = map(int, input().split())
    # 이용계획
    plan = list(map(int, input().split()))

    visited = [0]*12

    min_total = 1000000000000000
    # 연간 이용권과의 비교는 마지막에
    bt(0,0)

    if min_total > year:
        min_total = year

    print(f'#{tc} {min_total}')
