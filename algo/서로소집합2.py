p = [0] * 7
rank = [0] * 7

# 1. 집합 초기화
def make_set(x):
    p[x] = x
    # 처음트리의 깊이는  0
    rank[x] = 0

# 2 대표를 찾는 연산
def find_set(x):
    # 경로 압축
    if x != p[x]:
        p[x] = find_set(p[x])

    return p[x]

# 반복문으로 하는경우
def find_set2(x):
    while x != p[x]:
        x = p[x]

    return x

# 3. 두 집합을 합치는 연산
def union(x,y):
    # x 집합의 대표와 y집합의 대표를 찾기
    x = find_set(x)
    y = find_set(y)

    p[find_set(y)] = find_set(x)


# 집합 초기화
for i in range(1,7):
    make_set(i)

union(1,3)
union(2,3)
union(5,6)
union(1,5)
print(p)
print(find_set(1))
print(p)
# 대표자를 찾으라고 할 때 갱신됨
print(find_set(2))
print(p)
print(rank)
