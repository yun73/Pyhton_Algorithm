import sys
input = sys.stdin.readline

def solve():
    N, K = map(int,input().split())
    students = list(map(int, input().split()))
    group = [0]*(N-1)
    for i in range(1,N):
        group[i-1] = students[i]-students[i-1]
    group.sort()
    # print(group)
    cost = sum(group[:N-1-(K-1)]) # 키 차이 큰 얘들을 혼자인 조가 되게
    return cost

print(solve())