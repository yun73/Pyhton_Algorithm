'''
1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
3. 판매는 얼마든지 할 수 있다.
'''

T = int(input())
for tc in range(1,T+1):
    N = int(input())    # N 일동안 매매
    prices = list(map(int, input().split()))  # N일 동안의 매매가

    # 젤 낮은 가격에 사서 젤 비싼 가격에 팔아야 함
    # 대신 2일에 사면 3일에만 팔 수 있음
    # 처음에 가격을 넣고 그다음 가격이 같거나 낮으면 매입 높으면
    # 최대 가격을 아니까 그 때만 팔도록 최대가격 지나면 최대가격 갱신?
    # 사는게 append 파는게 pop
    max_price = 0
    max_day = 0
    for day in range(len(prices)):
        if max_price < prices[day]:
            max_price = prices[day]
            max_day = day

    buy = []
    profit = 0

    for price in prices:
        if len(buy) < 1:   # 처음 또는 다시 살 때
            if price == max_price:  # 가격이 최대가격이면 아무것도 안하는게 이득
                if max_day <= len(prices):  # 근데 아직 남은 날이 많으면
                    max_price = 0       # 남은 구간에서 최대 가격,날 다시 구해서 반복
                    for after in range(max_day + 1, len(prices)):
                        if max_price < prices[after]:
                            max_price = prices[after]
                            max_day = after
                else:
                    break
            else:
                buy.append(price)   # 가격이 최대 가격이 아니면 사재기

        else: # 처음 사는게 아닐때 이제부터 파는거 가능
            if price != max_price: # 최대가격 아닐 때는 사재기
                buy.append(price)
            else: # 최대 가격이면 팔아버려, 이후에 최대가격 갱신 필요
                my = len(buy)
                for i in range(my):
                    sell = buy.pop()  # 팔 거 빼내고
                    profit += (max_price - sell) # 최대가격과의 차이 만큼 이윤윤                # 다 팔아버렸는데 뒤에 남았을 때 위의 과정을 반복해서 그 다음 최대값에서 팔아줘야 해
                # 남은 범위는 max_price 등장 이후
                if max_day <= len(prices):
                    max_price = 0
                    for after in range(max_day+1, len(prices)):
                        if max_price < prices[after]:
                            max_price = prices[after]
                            max_day = after

    print(f'#{tc} {profit}')
