T = int(input())
for tc in range(1,T+1):
    str1 = input() # 찾을 문자열
    str2 = input() # 비교 문자열
    max_word = ''
    max_count = 0 # 문자 최대 개수
    for s1 in str1: # 찾을 문자를 하나씩 뽑아서
        count = 0
        for s2 in str2: # 비교할 문자열에서 하나씩 뽑아서 비교
            if s1 == s2: # 같으면
                count += 1  # s1 의 count가 증가
        if max_count < count: # 카운트가 max_count 보다 크면 max_count 갱신
            max_count = count
            max_word = s1

    print(f'#{tc} {max_count}')
    print(f'#{tc} {max_word}')

