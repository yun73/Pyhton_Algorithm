# A -> B

A, B = map(int, input().split())

# 연산횟수
cnt = 1

while B != A :
    if B<A:
        cnt = -1
        break

    if B % 2 == 0:
        cnt += 1
        B //= 2
    elif B%10 == 1:
        cnt += 1
        B //= 10
    else:
        cnt = -1
        break

print(cnt)