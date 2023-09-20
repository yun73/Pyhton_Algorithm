# 자연수 N에 몇 번의 연산을
# 자연수 M을 만들어보자
# 사용가능한 연산 = +1, -1, *2, -10
# 최소 몇번의 연산??
from collections import deque

# N : 연산결과
# M : 찾아야할 값
# cnt : 지금까지 연산횟수
# 중간 연산 결과 1000000 초과 시 도 고려

def bfs(res,M):
    global visited

    # 지금 내 연산결과에서 가능한 다음 값들을 저장해서 넘겨줘
    while res:
        # 현재 계산된 연산값
        now,cnt = res.popleft()
        # 새로운 리스트에 값을 담아줘
        cnt_now = cnt + 1
        for i in ['+1','*2','-1','-10']:
            # cal = eval(str(now)+i)
            if i == '+1':
                cal = now + 1
            elif i == '*2':
                cal = now * 2
            elif i == '-1':
                cal = now - 1
            elif i == '-10':
                cal = now - 10
            if 0< cal <= 10**6 and not visited[cal]:
                visited[cal] = True
                res.append((cal,cnt_now))
                if visited[M]:
                    return cnt_now


T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())

    visited = [False] * (1000000+1)
    visited[N] = True
    res = deque([(N,0)])
    print(f'#{tc} {bfs(res,M)}')


