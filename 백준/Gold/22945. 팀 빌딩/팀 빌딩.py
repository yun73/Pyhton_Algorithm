'''
팀빌딩

- 개발자 : N 명

- 팀 : 반드시 개발자 2명
    - 개발자 A, B
        - (개발자 A와 개발자 B 사이에 존재하는 다른 개발자 수) × min(개발자 A의 능력치, 개발자 B의 능력치)

- 팀 빌딩에서 나 올 수 있는 팀 중 능력치의 최대값

- A 개발자 위치를 a
- B 개발자 위치를 b 라 할 때
- 능력치가 최대가 되기 위해서는 최소값이 커야 하므로
- 둘 중 작은 걸 옮기면서 큰걸 찾아가자
두 위치의 능력치중 작은쪽의 인덱스를 1만큼 조작

'''

N = int(input())
X = list(map(int, input().split()))
a = 0
b = N-1
max_ability = (b-a-1)*min(X[a], X[b])
while a < b:
    # 두 개발자 사이의 다른 개발자 수
    p = b-a-1
    # 작은 쪽 숫자의 인덱스 조작
    if X[a] <= X[b]:
        # 둘 중 최소 능격치
        x = X[a]
        a += 1
    else:
        x = X[b]
        b -= 1

    # 팀능력치 계산 후 갱신
    ability = p * x
    if max_ability < ability:
        max_ability = ability

print(max_ability)