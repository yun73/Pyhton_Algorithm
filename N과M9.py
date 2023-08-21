# N 과 M

def perm(r,M,mc):
    if r == M: # M개의 원소를 고르면
        su = [0] * M
        for i in range(M):
            for j in range(0,N):
                if nums[i][j] == 1:
                    su[i] = num[j]
        if su in suli:
            return
        else:
            suli.append(su)
            print(*su)
        return
    else:
        for c in range(0,N):
            if r == 0:
                if nums[r][c] != 1:
                    nums[r][c] = 1
                    mc = c
                    perm(r+1, M, mc)
                    nums[r][c] = 0 # 포함할 때 다 탐색하고 돌아와서
                    # 0으로 바꾸고 다음열 탐색 ex) 3 2> 11,12,13 탐색후
                    # 시작부분 1인거 다 끝나고 시작부분 2부터
            else:
                if nums[r-1][c] != 1:
                    nums[r][c] = 1
                    mc = c
                    perm(r+1, M, mc)
                    nums[r][c] = 0 # 포함할 때 다 탐색하고 돌아와서
                    # 0으로 바꾸고 다음열 탐색 ex) 3 2> 11,12,13 탐색후
                    # 시작부분 1인거 다 끝나고 시작부분 2부터

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
# 1 부터 N 까지의 숫자중 중복 안하게 M 개 골라야 하므로
# 1~N 까지의 리스트 M 개 인 배열 생성
nums = [[0]*N for _ in range(M)]
# print(nums)
suli = []
perm(0,M,0)

