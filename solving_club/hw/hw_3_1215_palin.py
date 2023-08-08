T = 10
for tc in range(1, T+1):
    N = int(input()) # 찾아야 하는 회문길이
    word = [input() for _ in range(8)]

    count = 0 # 회문 누적 개수
    for i in range(8):
        for j in range(8-N+1): # 탐색 범위가 회문 길이 N-1만큼 감소한데까지만 가능
            if word[i][j] == word[i][j+N-1]: # 현재 위치 글자가 N번째 글자와 같으면 회문 검사
                for n in range(0, N//2 + 1):
                    if word[i][j+n] != word[i][j+N-1-n]:
                        break
                else:
                    count += 1

            if word[j][i] == word[j+N-1][i]:
                for n in range(0, N//2 + 1):
                    if word[j+n][i] != word[j+N-1-n][i]:
                        break
                else:
                    count += 1

    print(f'#{tc} {count}')

