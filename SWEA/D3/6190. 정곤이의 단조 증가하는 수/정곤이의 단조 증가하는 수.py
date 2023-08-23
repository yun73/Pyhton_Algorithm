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
    # 숫자가 하나만 주어지는 경우 처리
    if N == 1:
        dan = str(A[0])
        if len(dan) == 1:
            # if max_dan < int(dan):
            #     max_dan = int(dan)
            break
        else:
            for d in range(1, len(dan)):
                if int(dan[d]) < int(dan[d - 1]):
                    break
            else:
                if max_dan < int(dan):
                    max_dan = int(dan)
    else: # 숫자 리스트 주어지면
        # i, j 에서 j는 항상 i보다 커야 되므로
        for j in range(N):
            for i in range(j): # i는 j전까지 순회
                dan = str(A[i] * A[j])
                if len(dan) == 1:
                    # if max_dan < int(dan):
                    #     max_dan = int(dan)
                    continue
                else: # 앞에 값이 뒤에거 보다 큰경우 단조 아니니까 종료시키고 다음
                    for d in range(1,len(dan)):
                        if int(dan[d]) < int(dan[d-1]):
                            break
                    else: # break 안나면 갱신하기
                        if max_dan < int(dan):
                            max_dan = int(dan)


    print(f'#{tc} {max_dan}')

