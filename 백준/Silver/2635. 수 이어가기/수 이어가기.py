'''
IM 대비 문제 풀기
'''
# 수 이어가기
N = int(input())
first = N
third = 0
max_second = 0
max_cnt = 0
# N//2 보다 작거나 같은 숫자들을 두번 째 수로 넣게 되는 경우 음수 일찍 나옴
# 따라서 탐색 범위는 N//2 보다 클 때
# 가장 길게 이을 수 있는 second를 찾자
for s in range(N // 2, N+1):
    cnt = 0  # 두번째 숫자가 s일 때 이은 수
    second = s
    while first - second >= 0:
        third = first - second
        first = second
        second = third
        cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt
        max_second = s
    # 각 second 검사 후 초기화
    first = N
# print(max_second)
# second 구했으니까 이제 해당 숫자 넣었을 때 나오는 숫자 출력
print(max_cnt+2)
num = [0] * (max_cnt+2)
num[0] = N
num[1] = max_second
for i in range(2, max_cnt+2):
    num[i] = num[i - 2] - num[i - 1]
print(*num)
