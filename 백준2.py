# 내려가기
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
# print(arr)
dpmax = [0,0,0]
dpmin= [0,0,0]

dpmax[0] = arr[0]
dpmin[0] = arr[0]
dpmax[1] = arr[1]
dpmin[1] = arr[1]
dpmax[2] = arr[2]
dpmin[2] = arr[2]
for r in range(1,N):
    arr = list(map(int, input().split()))
    # print(arr)
    # 이걸 외부에다가 놓으면 안됨
    new_dpmax = [0, 0, 0]
    new_dpmin = [0, 0, 0]
    new_dpmax[0] = max(dpmax[0], dpmax[1]) + arr[0]
    new_dpmin[0] = min(dpmin[0], dpmin[1]) + arr[0]
    new_dpmax[1] = max(dpmax[0], dpmax[1], dpmax[2]) + arr[1]
    new_dpmin[1] = min(dpmin[0], dpmin[1], dpmin[2]) + arr[1]
    new_dpmax[2] = max(dpmax[1], dpmax[2]) + arr[2]
    new_dpmin[2] = min(dpmin[1], dpmin[2]) + arr[2]
    dpmax = new_dpmax
    dpmin = new_dpmin
    # print(dpmax)
    # print(dpmin)
print(max(dpmax[0], dpmax[1], dpmax[2]),min(dpmin[0], dpmin[1], dpmin[2]))
