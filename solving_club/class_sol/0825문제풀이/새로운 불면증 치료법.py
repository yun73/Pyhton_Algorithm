# 불면증
# 양세기 한대
# N 의 배수번호인 양을 셀거야
# k*N 번 양을 셀때 해당 숫자의 각 자리수가 누적되서 0~ 9 까지 다 나올때 멈춘다
# 최소 몇번을 세면 0~9 까지 다나올까
T = int(input())
for tc in range(1,T+1):
    # 양 셀 배수
    N = int(input())
    number = [0] * 10
    k = 1 # k번째 양을 셈
    while 0 in number:
        num = str(k * N)
        for i in num:
            if number[int(i)] != 1:
                number[int(i)] = 1
        k += 1

    print(f'#{tc} {(k-1)*N}')


'''
5
1
2
11
1295
1692
'''