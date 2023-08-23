'''
IM 대비 문제 풀기
'''
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # 주어지는 N 개의 수
    A = list(map(int, input().split()))
    # Ai * Aj 가 단조 증가인 증 4 7 이면 28처럼 단조증가
    # 단조증가는 다음위치 값이 지금거보다 크거나 같아야 함
    max_dan = -1
    if N == 1:
        dan = str(A[0])
        if len(dan) == 1:
            if max_dan < int(dan):
                max_dan = int(dan)
        else:
            for d in range(1, len(dan)):
                if int(dan[d]) < int(dan[d - 1]):
                    break
            else:
                if max_dan < int(dan):
                    max_dan = int(dan)
    else:
        for j in range(N):
            for i in range(j):
                dan = str(A[i] * A[j])
                if len(dan) == 1:
                    if max_dan < int(dan):
                        max_dan = int(dan)
                else:
                    for d in range(1,len(dan)):
                        if int(dan[d]) < int(dan[d-1]):
                            break
                    else:
                        if max_dan < int(dan):
                            max_dan = int(dan)


    print(f'#{tc} {max_dan}')

