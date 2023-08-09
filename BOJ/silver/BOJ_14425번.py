N, M = map(int, input().split())
S = [input() for _ in range(N)]
text = [input() for _ in range(M)]

count = 0

for word in text: # 찾을 문자열
    for s in S:   # 전체 문자열 하나씩 꺼내서
        if len(word) != len(s):  # 단어 길이가 더 크면 틀리다는거니까 다음거
            continue
        for i in range(len(s)-len(word)+1):   #단어 길이 고려해서 탐색
            if word[0] == s[i]:
                for j in range(len(word)-1,0,-1):
                    if word[j] != s[i+j]:
                        break
                else:
                    count += 1
            else:
                continue

print(count)

for word in text: # 찾을 문자열
    for s in S:   # 전체 문자열 하나씩 꺼내서
        if len(word) == len(s):
            if word == s:
                count += 1
        else:
            continue
print(count)

