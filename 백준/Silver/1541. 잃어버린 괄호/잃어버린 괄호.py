# 처음 수는 무조건 숫자
# -와 -or 끝 사이는 더해줘서 빼주면 무조건 최소값
susik = list(input().split('-')) # '-'로 나눠서 + 묶음 덩어리 리스트 생성
result = 0
for i in range(len(susik)):
    # 각 묶음을 '+'로 나눠서 더한값을 최종 계산값에다가
    sik = map(int,susik[i].split('+'))
    if i == 0:
        result += sum(sik)
    else:
        result -= sum(sik)

print(result)
