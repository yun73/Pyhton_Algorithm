'''
IM 대비 문제 풀기
'''
# 스위치 끄고 켜기
# 1 : 켜짐 , 0 : 꺼짐
# 스위치 개수, 100이하 양의 정수
N = int(input())
# 각 스위치의 상태
switch = [-1] + list(map(int, input().split()))
# 학생수
num = int(input())
for _ in range(num):
    # 학생의 성별, 받은 수
    # 1 : 남학생, 2 : 여학생
    gender, s = map(int, input().split())
    # 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
    # 여학생은 자기가 받은 수와 같은 번호 위치에서 좌우로 회문 판별 최대로 하고 바꾸기
    if gender == 1:  # 남자일 때
        for i in range(s, N+1, s):
            # 바꾸는거 mod 연산으로 하자
            switch[i] = (switch[i] + 1) % 2
    else:  # 여자일 때
        switch[s] = (switch[s] + 1) % 2
        left = s - 1
        right = s + 1
        while 1 <= left < s and s < right <= N and switch[left] == switch[right]:
            switch[left] = (switch[left] + 1) % 2
            switch[right] = (switch[right] + 1) % 2
            left -= 1
            right += 1

# 0번 인덱스 없애기
switch.pop(0)
for i in range(0,N,20):
    print(*switch[i:i+20])
