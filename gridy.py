'''
코딩 테스트 기초
1
시간 1초, 메모리 128MB

n : 2와 5로 나누어 떨어지지 않는 정수
각 자릿수가 모두 1로만 이루어진 n의 배수 중 가장 작은수

# 문제점
- 확인할 숫자를 1씩 늘려가게 되면 int 범위 벗어남
# 해결법
- 그 때다
'''
while True:
    try:
        n = int(input())
    except:
        break

    # i : 자릿수
    i = 1
    # (a*b)%c == (a%c*b%c)%c
    num = 0
    while True:
        num = num*10+1
        num %= n
        if num == 0:
            print(i)
            break
        i += 1

'''
검산
- n==3, i ==1, num == 0
- num == 0*10+1 == 1
1 %= 3 >> num== 1
if num!=0이므로 i +=1 >> i == 2
- num == 1*10+1 == 11
11%=3 >> num== 2
if num!=0이므로 i +=1 >> i == 3
- num == 2*10+1 == 21
21%=3 >> num==0
if num==0이므로 print i == 3, break
'''