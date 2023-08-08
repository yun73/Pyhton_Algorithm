# 행방향 회문검사
def palin_row(word, M, i, j):
    pal = ''
    for n in range(M // 2 + 1): # 회문이면 중간까지 양끝에서 부터 검사하면
        if word[i][j + n] != word[i][j + M - 1 - n]: # 이게 모두 break 당하지 않아야 함
            break
    else:
        for p in range(M): # break 안당하고 통과하면 회문
            pal += word[i][j + p] # 임시pal에 회문 단어들을 추가
        return pal # 회문인 pal 반환
    return pal # 회문아닌 pal 반환

# 열방향 회문검사
def palin_col(word, M, i, j):
    pal = ''
    for n in range(M // 2 + 1):
        if word[j + n][i] != word[j + M - 1 - n][i]:
            break
    else:
        for p in range(M):
            pal += word[j + p][i]
        return pal
    return pal



T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # NxN 크기의 배열, 길이 M인 회문찾기
    word = [list(input()) for _ in range(N)]

    # 회문 1개만 존재함
    # palin = [] # 이거는 회문 여러개일떄

    pal_word = ''

    for i in range(N):
        if pal_word != '':
            break
        for j in range(N - M + 1):  # 검사 길이 M 이므로 N-M+1 범위까지만 검사가능

            pal_word = palin_row(word, M, i, j) #회문 검사 결과 저장
            if pal_word != '': # 회문이면
                print(f'#{tc} {pal_word}')  # 회문인 결과 출력
                break

    if pal_word != '': # 행 검사 때 회문이 나오면 다음 테스트 케이스로
        continue
    else:
        for i in range(N):
            if pal_word != '':
                break
            for j in range(N - M + 1):  #

                pal_word = palin_col(word, M, i, j)
                if pal_word != '':
                    print(f'#{tc} {pal_word}')
                    break
