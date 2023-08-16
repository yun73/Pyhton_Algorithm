# N 과 M

def perm(r,M,mc):
    if r == M: # M개의 원소를 고르면
        for i in range(M):
            for j in range(1,N+1):
                if nums[i][j] == 1:
                    print(j, end = ' ')
        print()
        return
    else:
        for c in range(1,N+1):
            if c >= mc: # 자기 자신보다 크거나 같은거에 대해서만
                nums[r][c] = 1
                mc = c
                perm(r+1, M, mc)
                nums[r][c] = 0 # 포함할 때 다 탐색하고 돌아와서
                # 0으로 바꾸고 다음열 탐색 ex) 3 2> 11,12,13 탐색후
                # 시작부분 1인거 다 끝나고 시작부분 2부터

N, M = map(int, input().split())
# 1 부터 N 까지의 숫자중 중복 가능하게 M 개 골라야 하므로
# 1~N 까지의 리스트 M 개 인 배열 생성
nums = [[0]*(N+1) for _ in range(M)]
# print(nums)
perm(0,M,1)

'''
3 1
1 2 3
o
  o 
    o 
    
3 2
1 2 3
o
1 2 3
o
  o  
    o
'''