# 컨테이너 운반
# N개의 컨테이너를 M대의 트럭으로
# 트럭당 1개의 컨테이너
# 적재용량 초과 컨테이너 운반 x
# A에서 B로 편도 한번만
# 이동한 화물 최대 중량 되도록
# 옮겨진 화물의 무게
# 한개도 못올리면 0 출력

T = int(input())
for tc in range(1,T+1):
    # N : 컨테이너 수,M : 트럭수
    N, M = map(int, input().split())
    # 화물의 무게
    weights = list(map(int, input().split()))
    # M개 트럭의 적재용량
    limit = list(map(int, input().split()))
    limit.sort(reverse=True)
    weights.sort(reverse=True)
    # 실린 무게
    total_W = 0
    # 트럭의 인데스 t
    t = w = 0
    while True:
        if t == M or w == N:
            break
        # 적재용량보다 작거나 같으면 가능
        if limit[t] >= weights[w]:
            total_W += weights[w] # 화물 하나 실고
            t += 1 # 트럭하나 보내
            w += 1 # 다음 화물 보자
        else: # 적재용량 보다 크면 실을수 있는 최대 화물 중량 인덱스 1 키워줘
            # 내림차순이므로 뒤에 트럭도 어짜피 못 실음
            w += 1

    print(f'#{tc} {total_W}')

