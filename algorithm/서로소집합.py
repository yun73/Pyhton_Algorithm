# p[x] => x의 부모
# p[x] == x => x 가 속한 집합의 대표가 x다.
# p[x] != x => x는 x가 속한 집합의 대표가 아니다.
p = [0] * 7

# 1. 집합 초기화
def make_set(x):
    # 집합을 처음 만들때는 집합에 속한 사람이 1명, 동시에 자기 자신이 대표
    p[x] = x

# 2. x 가 속한 집합의 대표를 얻는 연산
def find_set(x):
    # 자기 자신의 부모가 자기 자신을 가르키고 있다면 자기자신이 대표
    if x == p[x]:
        return x
    # 그게 아닌 경우 부모의 대표를 찾는 것을 반복
    else:
        return find_set(p[x])
    

# 3. 두 집합을 합치는 연산
# x 가 속한 집합과 y가 속한 집합을 합치는 연산
# x 가 속한 집합의 대표와 y가 속한 집합의 대표 둘중에 하나로 대표를 통일
def union(x,y):

    p[find_set(y)] = find_set(x)


# 집합 초기화
for i in range(1,7):
    make_set(i)

union(1,3)
union(2,3)
union(5,6)
print(p)
