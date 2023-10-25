'''
곱셈
- 자연수 A를 B 번 곱한 수를 C로 나눈 나머지

- 나머지 연산
(A + B) % p = ((A % p) + (B % p)) % p
(A * B) % p = ((A % p) * (B % p)) % p
(A - B) % p = ((A % p) - (B % p) + p) % p

- 이대로 하면 시간초과 2,147,483,647 번 계산이어서

- B 는 짝수
    - A^B= A^B//2 * A^B//2
- B 는 홀수
    - A^B = A^B//2 * A^B//2 * A
- B를 절반으로 계속 나눠주면서
- 짝수일 떄와 홀수 일 때 연산을 다르게 해준다
'''
A,B,C = map(int, input().split())

def mod_cal(a,b,c):
    # 가장 작은 단위 이면
    if b == 1:
        return a%c

    # 홀수이면
    if b%2:
        return ((mod_cal(a,b//2,c)**2)*a)%c
    # 짝수이면
    else:
        return (mod_cal(a,b//2,c)**2)%c

print(mod_cal(A,B,C))