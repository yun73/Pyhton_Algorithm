'''
동전의 금액
가지고 있는 큰 금액의 동전부터 사용하고
그걸로 나눈 나머지가 남은 돈이므로
남은돈을 남은 동전들을 이요해서 또 계산해준다

(1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)
'''
from collections import deque

N, K = map(int, input().split())

coins = deque()

for _ in range(N):
    coin = int(input())
    coins.appendleft(coin)

res = 0
for coin in coins:
    # 만약 금액보다 작거나 같은 코인이 나오면
    if K >= coin:
        res += K // coin # 금액을 코인으로 나누 몫 = 사용한 해당 코인의 개수
        K %= coin # 금액을 코인으로 나눈 나머지 = 남은 금액
        # 만약 K 가 0이면 반복문 종료
        # coin[-1] 은 항상 1 이므로 무조건 금액을 맞출 수 있음
        if K==0:
            break

print(res)