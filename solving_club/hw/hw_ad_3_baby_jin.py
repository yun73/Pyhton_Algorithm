
def is_run(player):
    # 연속된 숫자 3개
    for i in range(0,8):
        if player[i] and player[i+1] and player[i+2]:
            return True
    else:
        False
def is_triple(player):
    # 3이 들어있으면 triple
    if 3 in player:
        return True
    else:
        return False

T = int(input())
for tc in range(1,T+1):
    number = list(map(int, input().split()))
    player1 = [0] * 10
    player2 = [0] * 10
    winner = 0
    for i in range(4):
        if i%2:
            player2[number[i]] += 1
        else:
            player1[number[i]] += 1

    for i in range(4,12):
        if i%2:
            player2[number[i]] += 1

        else:
            player1[number[i]] += 1

        if is_triple(player1) or is_run(player1):
            winner = 1
            break

        if is_triple(player2) or is_run(player2):
            winner = 2
            break
    print(f'#{tc} {winner}')
