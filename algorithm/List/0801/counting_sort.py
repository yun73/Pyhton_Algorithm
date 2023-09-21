# 원본의 순서 바뀌지 않음

def Counting_Sort(A, B, k):
    # A [] 입력배열, 정렬 대상
    # B [] 정렬된 배열
    # C [] 카윤트 배열

    C = [0] * (k + 1)
    # C :  카운트 배열(원소의 개수를 세주고, 자리를 정해준다.)
    # C[i] = i 의 등장횟수

    # 각 원소의 등작 횟수 세준다.
    for i in range(len(A)):
        # C[A[i]] += 1
        C[A[i]['num']] += 1
    # 각 원소의 등장횟수 계산 후, 각 원소 들어갈 자리 위치 구하기
    for i in range(1, len(C)):
        # i는 i보다 작은 수가 몇개 있는 지를 알면 그 뒤부터 나온다는걸 알기 떄문에
        C[i] += C[i - 1]

    # 뒤에서부터 A를 확인하면서 자리를 확인하고 채워준다.
    # 뒤에서 부터 하는 이유는 안정 정렬(원래 배열의 순서 보장)
    # 자리를 채워줄 때마다 1씩 감소시켜줘야 한다. (자리 중복 피하기 위해서)
    for i in range(len(B) - 1, -1, -1):
        # C[A[i]] => A[i] 가 들어갈 자리를 가르킴 들어가기전에 1뺴기
        # C[A[i]] -= 1
        C[A[i]['num']] -= 1
        # 자리에 A[i] 넣어주기
        # B[C[A[i]]] = A[i]
        B[C[A[i]['num']]] = A[i]


nums = [1, 0, 3, 4, 7, 3, 2]
nums_dict = [
    {'name': '김', 'num': 1},
    {'name': '조', 'num': 0},
    {'name': '강', 'num': 3},
    {'name': '신', 'num': 4},
    {'name': '김', 'num': 7},
    {'name': '박', 'num': 3},
    {'name': '이', 'num': 2},
]

result_asc = [0] * 7
Counting_Sort(nums_dict, result_asc, max(nums))
print(result_asc)


# 카운팅 정렬 내림차순

def Counting_Sort_des(A, B, k):
    # A [] 입력배열, 정렬 대상
    # B [] 정렬된 배열
    # C [] 카윤트 배열
    C = [0] * (k + 1)

    for i in range(0, len(A)):
        C[A[i]] += 1

    # 내림 차순으로 하려면 개수가 1, 2, 1, 3 일 때 오름차순(1,3,4,7)과 반대로 누적해야함 (7,6,4,3)
    for i in range(len(C) - 2, -1, -1):
        C[i] += C[i + 1]

    for i in range(len(B) - 1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]


nums = [1, 0, 3, 4, 7, 3, 2]
result_asc = [0] * 7
Counting_Sort_des(nums, result_asc, max(nums))
print(result_asc)
