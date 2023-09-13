'''
L : 커서를 완쪽으로 한칸(맨 앞이면 무시)
D : 커서를 오른쪽으로 한칸(맨뒤 무시)
B : 커서 왼쪽 문자삭제 (커서 문장 맨앞이면 무시)
P $: $ 문자 커서 왼쪽에 추가
'''
# 맨 뒤 커서 시작 명령다 수행하고 입력된 문자열 구해
import sys

# 스택두개 사용
# 커서 이동은 left 커서 right
# 왼쪽 이동이면 왼쪽거 마지막을 오른쪽 처음으로

# 입력 문자열
# 스택
left = list(input())
# 뒤집은걸로 생각 그래야 커서 왼쪽 두번 이동하고 오른쪽 이동시 마지막에 넣을걸 꺼내옴
right = []
# 문자열 길이
N = len(left)
#명령어 개수
M = int(sys.stdin.readline())

for _ in range(M):
    command = list(sys.stdin.readline().rstrip().split())
    if command[0] == 'L' and left:
        right.append(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])

answer = left + right[::-1]
print(''.join(answer))
