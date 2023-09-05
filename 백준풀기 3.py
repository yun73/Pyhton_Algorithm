# 단어 뒤집기
import sys
# 입력값 받는 시간 줄이기 위해서
T = int(sys.stdin.readline())
for tc in range(1, T+1):
    # 공백을 기준으로 단어를 구분하여 입력받기
    words = sys.stdin.readline().split()
    # print(words)
    for i in range(len(words)): # 단어 개수만큼 반복
        # 각 단어들을 뒤집어서 출력, 끝에 공백으로 이어주기
        print(words[i][::-1], end= " ")
    # 한문장 출력 끝나면 줄바꿈
    print()

'''
2
I am happy today
We want to win the first prize

'''