# 숨바꼭질 6

def gcd(a,b):
    # 종료 조건
    if b == 0:
        return a
    # 재귀 호출
    else: # 대소비교가 나머지 연산으로 해결됨
        return gcd(b, a % b)

# N 명의 동생,S 수빈이의 현재 위치
N, S = map(int,input().split())
# 동생의 위치
A = list(map(int,input().split()))
# 1초 후 +-D 만큼 움직일 수 있음
# 시간 상관없이 D의 최대값

# 동생들과의 위치 차이의 최대 공약수

distance = abs(A[0]-S)
for a in A:
    distance = gcd(abs(a-S), distance)

# 최대공약수 다 구했으면 거리 하나만 남아있을 거임
print(distance)



