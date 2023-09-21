# N-queen 알고리즘
# 일반 백트래킹 알고리즘
# n*n의 정사각형 안에 n 개의 queen을 배치하는 문제
# 모든 queen은 자신의 일직선상 및 대각선상에 아무것도 놓이지 않아야 함
'''
def checknode(v): # node
    if promising(v):
        if there is a solution at v:
            write the solution
        else
            for u in each child of v:
                checknode(u)
'''
# 이전에 검사하여 불가능한 곳은 사전에 차단하여 DFS보다 효율적