
import sys
input = sys.stdin.readline

def solve():
    N, K = map(int,input().split())
    students = list(map(int, input().split()))
    group = [students[i+1]-students[i] for i in range(len(students)-1)]
    group.sort()
    for i in range(K - 1):
        group.pop()
    return sum(group)

print(solve())