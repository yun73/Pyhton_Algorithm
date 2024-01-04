import sys
input = sys.stdin.readline

max_num = -1
ans_x,anx_y = 0,0
for i in range(9):
    nums = list(map(int, input().split()))
    for j in range(9):
        if nums[j] > max_num:
            max_num = nums[j]
            ans_x,anx_y = i,j
            
print(max_num)
print(ans_x+1,anx_y+1)