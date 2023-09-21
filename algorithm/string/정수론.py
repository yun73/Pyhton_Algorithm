# 최대 공약수 GCD : Greatest Common Dvisor
# 최소 공배수 LCM : Least Common Multiple

# 최대 공약수
# a > b
def gcd(a, b):
    for i in range(b, 0,-1):
        if a % i == 0 and b % i == 0:
            return i

# 유클리드 호제법
# a, b 의 최대 공약수 구하기
# a > b
# a 와 b, a를 b로 나눈 나머지 r 이 있다고 했을 때 다음이 성립한다.
# a와 b의 최대 공약수는 b와 r의 최대 공약수와 같다.
# 재귀적으로 (a,b) == (b,r)
# new_gcd(a,b) == new_gcd(b,r)

def new_gcd(a,b):

    # 종료 조건
    if b == 0:
        return a
    # 재귀 호출
    else:
        return new_gcd(b, a % b)

# 최소공배수
# a와 b의 최소공배수는 a와 b의 곱을 최대공약수로 나눈 것과 같다.
def lcm(a, b):
    return a*b // new_gcd(a,b)

a= 20
b =15
print(new_gcd(a,b))
print(lcm(a,b))