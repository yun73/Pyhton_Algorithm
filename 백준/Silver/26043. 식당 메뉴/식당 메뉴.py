'''

식당 줄 서기

식사 1인분 씩

맨 앞의 학생 한명 들어가서 식사 시작

두가지 메뉴 중 하나 먹음

S : 식사가 준비되는 n 개의 정보

A : 본인이 좋아하는 메뉴를 먹은 학생 목록
B : 본잉이 좋아하지 않는 메뉴를 먹은 학생 목록
C : 식당 도착 후 식사 못한 학생

'''
import heapq, sys
from collections import deque
input = sys.stdin.readline

students = {0:[], 1:[], 2:[]}
wait = deque([])
n = int(input())
for i in range(n):
    info = list(map(int, input().split()))

    if info[0] == 1:    # 만약 들어온 값이 유형 1이라면
        wait.append((info[1:3]))
    else:   # 만약 들어온 값이 유형 2 라면
        student_id, menu = wait.popleft()
        if info[1] == menu:
            students[0].append(student_id)
        else:
            students[1].append(student_id)
if wait:
    students[2] += [id for id,menu in wait]

for i in range(3):
    if len(students[i]) > 0:
        print(*sorted(students[i]))
    else:
        print('None')