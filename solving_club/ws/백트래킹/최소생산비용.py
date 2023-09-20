# 최소생산비용
# N 종의 제품을 N 곳의 공장, 한곳당 한가지 생산
# 공장별 생산비용 주어짐

# r : 생산할 제품
# N : 생산이 정해진 제품의 개수 도달점
# price : 각 제품당 정해진 생산공장 비용들의 현재까지의 합
def bt(r,N,price):
    global min_price
    global select

    # 종료조건 : 3번 제품까지 어느 공장에서 생산할지 다 정했을 때
    if r == N:
        # 지금까지의 비용이 최소면 갱신
        if min_price > price:
            min_price = price   
        return
    
    # 가지 치기
    # 만약 지금까지의 합이 최소 합보다 크거나 같다면 그냥 리턴 시켜버려
    if price >= min_price:
        return

    # 재귀호출 로직
    # N 개의 공장 중 하나를 선택했을 때
    for c in range(N):
        # 아직 뭐 생산할지 안정해졌으면
        if not select[c]:
            # 해당 열에 해당하는 제품 생산하고
            select[c] = True
            # 다음거 고르러 가보자
            bt(r+1,N,price + V[r][c])
            # 돌아오면 여기말고 다른데서도 생산해보자
            select[c] = False


T = int(input())
for tc in range(1,T+1):
    # 제품수, 공장수
    N = int(input())
    # 제품당 공장별 생산비용 V
    V = [list(map(int, input().split())) for _ in range(N)]
    # 최소 생산 비용
    min_price = 99*(N**2) + 1
    # 생산할 제품이 정해진 공장
    select = [False] * N

    bt(0,N,0)

    print(f'#{tc} {min_price}')