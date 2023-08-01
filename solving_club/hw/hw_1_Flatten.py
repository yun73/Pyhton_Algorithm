# 높은 곳 상자 낮은곳으로 => 평탄화(최고점과 최저점 간격 줄이기)
# 평탄화 수행시 고, 저 차이 1 이내
# 덤프 : 가장 높은 곳 상자 낮은곳으로
# width = 100, height 1~ 100, dump_n 1 ~ 1000
# dump 이내 평탄화 완료시 그 때의 고저 차이 반환
# T = 10
T = 10
for tc in range(1,T + 1):
    dump_limit = int(input())
    box = list(map(int, input().split()))
    