N, M = map(int, input().split())
N_list = list(range(1,N+1))

nums = [] # 부분집합 넣을 저장소
for i in range(1<<N):
    num = []
    for j in range(N):
        if i & (1<<j):
            num.append(N_list[j])
    if len(num) == M: # 길이가 M인 부분집합, 오름차순으로 정렬된 숫자들을 가져와 마지막에 추가함
        nums.append(num)
# print(nums)

# nums안의 리스트들의 첫번째 숫자에 따라 오름차순정렬
for i in range(len(nums)-1,0,-1):
    for j in range(0, i):
        if str(nums[j]) > str(nums[j+1]):
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

for num in nums:
    print(*num)


