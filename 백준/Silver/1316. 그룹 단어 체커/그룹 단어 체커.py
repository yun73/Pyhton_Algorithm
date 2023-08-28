# 그룹단어 체커
# 단어의 개수
N = int(input())
# 그룹단어의 개수
cnt = 0
for tc in range(N):
    word = input()
    # 한글자이면 무조건 맞음
    if len(set(word)) == 1:
        cnt += 1
        continue
    elif len(set(word)) == len(word):
        cnt += 1
        continue
    else:
        check = []
        # 맨 앞단어 넣어두자
        check.append(word[0])
        # 단어 앞에서 부터 확인
        for i in range(1,len(word)):
            if word[i] != word[i-1]:
                # 앞에 단어랑 다를때 이미 나온적이 있으면 그룹단어 아님
                if word[i] in check:
                    break
                else:
                    check.append(word[i])
        else:
            cnt += 1

print(cnt)