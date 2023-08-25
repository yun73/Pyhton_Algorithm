
T = int(input())
for tc in range(1,T+1):
    # 만들어진 단어 여러줄로 주어짐
    word = [input() for _ in range(5)]
    # 글자 개수 다를 수 있다
    # 각 열 번호에 해당하는 순서에 위에서 부터 차레대로 넣어주자
    order = [[] for _ in range(15)]
    # 단어 세로로 읽기. 왼쪽부터 위 > 아래
    for w in word: # 한줄씩 받아와서
        for i in range(len(w)):
            order[i].append(w[i])
    # 세로로 읽은 순서대로 글자들을 출력
    print(f'#{tc}', end = ' ')
    for cword in order:
        print(''.join(cword), end ='')

    print()
