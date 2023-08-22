'''
IM 대비 문제 풀기
'''
# 패턴 마디의 길이
T = int(input())
for tc in range(1, T+1):
    string = input()
    # 마디의 길이
    result = 0
    for t in range(1,11):
        pattern = []
        if string[0] == string[t]:
            # 같은 문자 만나면 그 전까지를 패턴 문자로 생각해보자
            for i in range(0,t):
                pattern.append(string[i])
            # t 부터 그 뒤에 패턴 길이만큼 같으면 마디 맞음
            i = 0
            for p in range(t,t+len(pattern)):
                if string[p] == pattern[i]:
                    i += 1
                else:
                    break
            else:
                # 마디 찾음
                result = len(pattern)
                break

    print(f'#{tc} {result}')
