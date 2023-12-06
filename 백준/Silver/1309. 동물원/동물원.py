N = int(input())

# 한줄당 타일 배치 방법 3가지로 고정
# 3가지에서 각각 놔둘수 있는 타일 배치도 2개나 3개로 고정 그러면
# 이전 결과에서 이어서 나올수 있는 각 타일의 전체개수를 구하기
arr = [1,1,1]
for i in range(1,N):
    new_arr = [0,0,0]
    new_arr[0] = arr[1] + arr[2]
    new_arr[1] = arr[0] + arr[2]
    new_arr[2] = sum(arr)
    arr = new_arr

print(sum(arr)%9901)


