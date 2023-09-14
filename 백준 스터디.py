# 동전
'''
문제 접근 방법
- 동전이 오름 차순으로 정렬되어 주어지기 때문에 작은 동전을 이용하여
m원을 만들 수 있는 경우의 수를 더하자, 다음 동전으로 넘어가서
이전경우의 수에 해당 동전으로 만들 수 있는 경우의 수를 순차적으로 더해ㅏ며 답을 구한다.
ai : 금액 i를 만드는 방법의 수
k : 각 화폐의 단위
점화식 : 각 화폐의 단위인 k를 돌면서 금액 1 ~ M 을 만들 수 있는지 확인한다
'''

T = int(input())
for tc in range(1,T+1):
    # 동전의 가지수
    N = int(input())
    # N가지 동전 오름차순으로 주어짐
    coins = list(map(int, input().split()))
    # 만들어야할 금액
    M = int(input())

    # memoization을 위한 리스트 선언
    dp = [0] * (M+1)
    dp[0] = 1

    for coin in coins:
        for i in range(M+1):
            # a_(i-k) 를 만드는 방법이 존재한다면
            # 이전 경우의 수에 현재 동전으로 만들 수 있는 경우의 수를 더한다.
            if i >= coin:
                dp[i] += dp[i-coin]

    print(dp)