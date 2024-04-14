'''
N : 1 ~ 80000
h : 1 ~ 1,000,000,000

자기보다 높이가 작으면서, 건물 번호가 커야 됨

이 건물을 볼 수 있는 빌딩의 개수를 세주면?
>> 지금까지 내 앞에 있는 건물들을 알아야 함
    >> 만약 지금 빌딩보다 스택의 마지막 빌딩이 작다면 제외
        : 어짜피 나보다 작은 빌딩은 이 이후를 못 봄
    >>
'''
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    H = [0] * N
    for i in range(N):
        H[i] = int(input())

    left = []
    cnt = 0
    for height in H:
        # 지금 빌딩 앞에 빌딩이 있고,마지막에 추가된 값이 나보다 작거나 같다면
        while left and left[-1] <= height:
            # 어짜피 이 이후는 못보니까 제거
            left.pop()
        # 현재 나를 볼 수 있는 건물 개수 추가
        cnt += len(left)
        # 현재 빌딩 추가
        left.append(height)

    return cnt

print(solve())