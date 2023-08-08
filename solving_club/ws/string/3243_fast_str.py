T = int(input())
for tc in range(1, T + 1):
    A, B = input().split()

    min_cnt = len(A)
    a = 0
    b = 0
    while a <= len(A) - len(B):
        if A[a] == B[b]:
            for i in range(1, len(B)):
                if A[a + i] != B[b + i]:
                    a += 1
                    b = 0
                    break
            else:
                min_cnt -= (len(B)-1)
                a += len(B)
                b = 0
        else:
            a += 1
            b = 0

    print(f'#{tc} {min_cnt}')


# T = int(input())
# for tc in range(1, T + 1):
#     A, B = input().split() # A는 타이핑할 문자열, B는 단어
#
#     min_cnt = len(A)  # 최소 타이핑 횟수 최대값인 길이만큼 설정
#     # 가지고 있는 단어가 문자열에 나올 때 마다 최소 타이핑 감소
#     for a in range(len(A)):
#         if A[a] == B[0]:
#             for b in range(1,len(B)):
#                 if A[a+b] != B[b]:
#                     break
#             else:
#                 min_cnt -= (len(B)-1)
#
#     print(f'#{tc} {min_cnt}')
