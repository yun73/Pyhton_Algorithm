N, S = map(int,input().split())
N_list = list(map(int, input().split()))

cnt = 0   # 조건 만족하는 부분집합 개수
nums = [] # 부분집합 넣을 저장소
for i in range(1<<N):
    num = []
    sub_sum = 0
    for j in range(N):
        if i & (1<<j):
            num.append(N_list[j])
            sub_sum += N_list[j]
    if sub_sum == S: #  합이 S 부분집합,
        nums.append(num)
        print(nums)
        cnt += 1

print(cnt)
