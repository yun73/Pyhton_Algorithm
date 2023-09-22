

# N : 동물 수, M : 사대 수 ,L : 사정거리
N, M, L = map(int,input().split())
location = [0] * (1000000000+1)
# 사대위치
gun = list(map(int, input().split()))
gun.sort()

# 잡는 개수
catch = 0
# 동물 위치
for i in range(N):
    x,y = map(int, input())
    if y > L:
        continue
    # 일단 입력 받으면서 사정거리 밖에 있는 얘들은 받지마




print(catch)