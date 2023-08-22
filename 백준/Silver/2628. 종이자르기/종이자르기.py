'''
IM 대비 문제 풀기
'''
# 종이자르기
# 가로, 세로
W, H = map(int, input().split())
# 점선의 개수
w_line = [0]
h_line = [0]
num = int(input()) # 점선 정보
for _ in range(num):
    # 가로점선 0, 세로점선 1, 몇번 라인
    dot, line = map(int, input().split())
    if dot == 0:
        h_line.append(line)
    else:
        w_line.append(line)

w_line.append(W)
h_line.append(H)
w_line.sort()
h_line.sort()
max_area = 0

for r in range(1,len(w_line)):
    for c in range(1,len(h_line)):
        area = (w_line[r]-w_line[r-1]) * (h_line[c]-h_line[c-1])
        if max_area < area:
            max_area = area

print(max_area)