# # 퀴즈 대회
# # 주어진 번호는
# # 십진수 각 자리 값
#
# T = int(input())
# for tc in range(1,T+1):
#     n, change = input().split()
#     num = list(n)
#     print(n)
#     print(num)
#     print(change)
#     # 최대값은 내림차순
#     # 최대값 됐을 때 남은 교환 횟수 짝수이면 종료
#     max_value = [] = num.sort(reverse=True)
#     # 최대값의 인덱스
#     m = 0
#     # 바꿀자리 인덱스
#

def swap(cnt):
    global max_pri
    # 종료 조건 : 교환 횟수를 다 소모 했다면
    # 바꾼 결과물을 숫자로 바꿔서 최대 상금 계산
    if cnt == N:
        result = int(''.join(S))
        if result not in create:
            create.append(result)
            if max_pri < result:
                max_pri = result

        return
    # 자리를 바꿀 위치 2개를 교환 한번 할 때 마다 새로 지정해줘야 한다.
    # 이 문제에서는 동일한 위치에서 중복교환을 허용
    # 바꿀 위치중에 앞쪽 : i
    # 바꿀 위치중에 뒤쪽 : j
    else:
        for i in range(len(S)-1):
            for j in range(i+1,len(S)):
                S[i], S[j] = S[j], S[i]
                swap(cnt+1)
                # 다시 되돌려 놓기
                S[i], S[j] = S[j], S[i]

T = int(input())
for tc in range(1,T+1):
    S, N = input().split()

    S = list(S)
    N = int(N)
    high = sorted(S,reverse=True)
    high_p = int(''.join(high))
    max_pri = 0
    create = []
    if len(S) < N: # 교환횟수가 문자길이보다 크거
        # 최대문자 무조건 나옴
        if (N-(len(S)-1)) % 2:  # 남은 횟수 홀수 이면
            if S[0] == [1]:  # 만약 맨 앞 두개가 같으면
                max_pri = high_p
            else:
                high[-1], high[-2] = high[-2], high[-1]
                result = int(''.join(high))
                max_pri = result

        else:  # 짝수이면 그냥 끝내도 됨
            max_pri = high_p

    else:
        swap(0)

    print(f'#{tc} {max_pri}')
