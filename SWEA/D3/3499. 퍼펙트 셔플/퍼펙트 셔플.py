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
    # 카드의 앞에서 부터 디큐하여 left, right 에 인큐
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
	# left, right에 저장된 카드 교대로 디큐하여 다시 카드에 인큐
    while left or right:
        card.append(left.pop(0))
        if right:
            card.append(right.pop(0))

    print(f'#{tc}', *card)