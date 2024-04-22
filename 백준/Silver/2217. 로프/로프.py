import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    rope = [0]*10001
    for i in range(N):
        rope[int(input())] += 1

    # 위에서 부터 내려오면 위에 얘들은 무조건 중량 들 수 있음
    max_weight = 0
    can_cnt = 0
    for i in range(10000,-1,-1):
        # 현재 중량 i 개
        can_cnt += rope[i]
        # 중량 = can_cnt * i
        max_weight = max(max_weight,can_cnt*i)

    return max_weight

print(solve())