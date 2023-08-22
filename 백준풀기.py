'''
IM 대비 문제 풀기
'''
# 퍼펙트 셔플
T = int(input())
for tc in range(1, T + 1):
    # N 개의 카드 주어짐
    N = int(input())
    card = list(input().split())
    left = []
    right = []
    if N % 2:
        for i in range(0, N // 2 + 1):
            left.append(card.pop(0))
        while card:
            right.append(card.pop(0))
    else:
        for i in range(0, N // 2):
            left.append(card.pop(0))
        while card:
            right.append(card.pop(0))

    while left or right:
        card.append(left.pop(0))
        if right:
            card.append(right.pop(0))

    print(f'#{tc}', *card)