def construct_candidates(a,k,in_val, c):

    in_perm = [False] * NMAX

    for i in range(1,k):
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(1,in_val+1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1

    return ncandidates

def backtrack(a, k ,in_val):
    global MAXCANDIDATES
    c= [0] * MAXCANDIDATES

    if k == in_val:
        process_solution(a,k) # 답이면 원하는 작업
    else: # 아니면 재귀호출하여 백트래킹
        k+=1  # +1 하고 2번째 칸부터 in_val 칸까지 1씩 증가하면서
        # 해당 칸에 있는 원소를 부분집합에 포합할건지 정함
        # 백트랙 하기위한 후보군을 구하는 함수
        ncandidates = construct_candidates(a,k,in_val,c)
        for i in range(ncandidates):
            a[k] = c[i] # c[0] True
            backtrack(a,k,in_val) # k = 1,2,3.., in_val = 3

def process_solution(a, k): # 1,2,3 출력
    print("(",end = "")
    for i in range(k+1):
        if a[i]: # a[i]에 저장된 값이 True 이면
            print(i, end = "")
    print(")")


in_val = int(input()) # 구하고 싶은 부분집합 원소의 개수
# 3개의 원소로 이루어진 파워셋 구하기
MAXCANDIDATES = 100
NMAX = 100
a = [0] * NMAX
backtrack(a, 0, 3)
