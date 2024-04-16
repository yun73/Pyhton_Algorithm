def solve():
    N, K, *students= map(int, open(0).read().split())
    group = [students[i+1]-students[i] for i in range(len(students)-1)]
    group.sort()
    for i in range(K - 1):
        group.pop()
    return sum(group)

print(solve())