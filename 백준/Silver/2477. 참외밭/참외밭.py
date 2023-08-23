'''
IM 대비 문제 풀기
'''
# 참외밭

# 1m^2 에 자라는 참외의 개수
K = int(input())
# 육각형의 임의의 한 꼭짓점에서 출발, 반시계방향
# 동 1 서 2 남 3 북 4
stack = []
# 이전 좌표 기억하기
br, bc = 0, 0
for _ in range(6):
    di, length = map(int, input().split())
    # 좌표 만들기
    if di == 4: # y축 방향 위로 가는거
        bc += length
    elif di == 3: # y축 방향 아래로 가는거
        bc -= length
    elif di == 2: # x축 방향 왼쪽으로 가는거
        br -= length
    elif di == 1: # x축 방향 오른쪽로 가는거
        br += length
    stack.append((br,bc))

# 면적 계산 위해 첫번째 좌표 추가
stack.append(stack[0])
stack.append(stack[5])
# print(stack)
# 면적 계산
# 육각형이므로 좌표 6개
area = 0
for i in range(6):
    area += stack[i][0]*(stack[i+1][1]-stack[i-1][1])

result = abs(area)//2 * K


print(result)