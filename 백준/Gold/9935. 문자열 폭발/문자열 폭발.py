'''
문자열 폭발

- 주어진 폭발 문자열이 있으면 해당 단어 제거

- split()하고 join : 매 번 O(N) 시간을 사용

- cc44 와 같이 찾는 문자열이  c4 일 때
- cc4 가 되는 순간 문자열이 있는 것을 판단할 수 있다.
- 그럼 이 때 찾는 문자열 들을 모두 제거해주고 - stack pop 사용
- 계속 이어간다
- 근데 다른 문자 나오면 다시 넣으면서
'''
import sys
input = sys.stdin.readline

str_li = input().rstrip()
find = input().rstrip()
# 확인된 문자열 저장
check  = []
# 36*1,000,000 = 360 만
for i in range(len(str_li)):
    # 내가 찾는 문자열이 아닌게 나오면 만약 그전까지 체크하던게 있다면 이어주자
    # 굳이 이 부분을 만들 필요가 없음
    # if str_li[i] not in find:
    #     if check:
    #         result += ''.join(check)
    #     result += str_li[i]
    #     continue
    # 만약 find 에 포함되는 문자열 이라면
    # 일단 체크 리스트에 넣고
    check.append(str_li[i])
    # 만약 넣는데 내가 찾는 문자열이 안에 있으면 뺴내자
    # in 연산시 check 안의 요소를 전부 도니까
    # 맨 뒤에서 찾는 문자열 길이 만큼이 찾는 문자열이면 으로 조건 수정
    if ''.join(check[-len(find):]) == find :
        for _ in range(len(find)):
            check.pop()

if check:
    print(''.join(check))
else:
    print('FRULA')