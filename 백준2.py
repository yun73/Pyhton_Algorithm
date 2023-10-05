'''
신기한 키보드

- 키보드
    - 버튼 3개
        - 왼쪽 : 왼쪽으로 커서 한칸
        - 오른쪽 : 오른쪽으로 커서 한칸
        - 엔터 : 문자열을 컴퓨터에 전송히여 컴퓨터 화면에 출력
    - LCD 창 1개
        - 문자열 S
        - 창 크기 : 문자열 S 와 정확하게 같음

- 커서 : 문지열의 가장 왼쪽 글자에 위치
    -  문자 위에 표시되고 해당하는걸 엔터 누르면 출력됨
    - LCD 창 벗어나지 않음

- 알파벳 순서로 출력, 키를 누르는 횟수의 최소값

- 알파벳 순서로 출력해야 하므로
    - a,b,c,.. 현재 찾아야할 알파벳을 알아야 함
    - 문자열 길이 최대 50
    - 찾은 문자는 빈칸이 됨
    - 찾으러 앞쪽과 뒤쪽 모두 가봐야됨
- 엔터키는 찾으면 무조건 누르는 거니까 일단 나중에 생각
- 그러면 내가 지금 보는 인덱스와 찾아야할 문자의 인덱스들을 알아야 한다.
- 문자가 모두 소문자 이므로 아스키 코드로
'''
word = {}
# 소문자 a~z
for i in range(97,123):
    word[chr(i)] = []
print(word)

S = list(input())
for i in range(len(S)):
    # 해당하는 알파벳의 인덱스를 추가
    word[S[i]].append(i)
print(word)
# 현재 커서 위치
cursor = 0
# 전체 클릭 횟수
total = len(S)
for i in range(97,123):
    is_clear = [0] * len(word[chr(i)])
    # 해당하는 문자를 다 출력할 때 까지 조작
    while 0 not in is_clear:
        # 현재 커서 위치와 가까운 걸 먼저
        min_sub = int(1e9)
        q = 0
        for j in range(len(word[chr(i)])):
            if is_clear[j]:
                continue
            if min_sub > abs(cursor - word[chr(i)][j]):
                min_sub = abs(cursor - word[chr(i)][j])
                q = word[chr(i)][j]

        total += (cursor - q)
        cursor = cursor - (cursor - q)

