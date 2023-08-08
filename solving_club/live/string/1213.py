T = 10
for t in range(1,T+1):
    tc = int(input())
    word = input() # 찾을 문자
    string = input() # 주어지는 문자열

    count = 0

    for i in range(len(string)-len(word)+1):
        if string[i] == word[0]:
            for j in range(1,len(word)):
                if string[i+j] != word[j]:
                    break
            else:
                count += 1

    print(f'#{tc} {count}')

T = 10
for t in range(1,T+1):
    tc = int(input())
    word = input() # 찾을 문자
    string = input() # 주어지는 문자열

    count = 0
    w = 0   # word의 인덱스
    s = 0   # string의 인덱스
    while s < len(string):
        if string[s] != word[w]:
            s = s - w + 1
            w = 0
        else:
            if w == len(word) - 1:
                count += 1
                s = s - w + 1
                w = 0
            else:
                s += 1
                w += 1






