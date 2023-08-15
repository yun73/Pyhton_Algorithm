# 부분집합의 수
# 원소가 n 개일 때, 부분집합 개수는 2**n 개
# 공집합을 포함
# def print_subset(bit, arr, n):
#     total = 0 # 부분집함의 함
#     for i in range(n):
#         if bit[i]:
#             print(arr[i], end = ' ')
#             total += arr[i]
#     print(bit, total)
#
# arr = [1,2,3,4]
# bit = [0,0,0,0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2]= k
#             for l in range(2):
#                 bit[3] = l
#                 print_subset(bit, arr, n)

# 비트 연산자
# 보다 간단하게 구현하는 방법
arr = [1,2,3,4,5,7]
n= len(arr)  # n 집합의 원소의 개수

# 모든 부분 집합 검사
# 1<<n 부분집합의 개수 2*n 이랑 똑같은 거임 2^6 == 1<<6 == 1*2^6
for i in range(1<<n):   # 부분 집합의 개수만큼 반복
    # i 번째 부분집합을 검사하겠다
    # i 번째 부분집합이 n개의 원소 중에 j 번쨰 원소를 포함하는지
    for j in range(n):  # 원소의 수만큼 비트를 비교 3<<4 == 3 * 2^4
        if i & (1 << j):  # 부분집합 i가 j번째 원소를 포함했는지 비트가 1인 경우
            print(arr[j],end =', ')  # j 번 원소 출력
    print()
print()
