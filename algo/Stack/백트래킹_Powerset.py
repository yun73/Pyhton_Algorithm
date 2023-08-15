'''
Power Set
어떤 집합의 공집합과 자기자신을 포함한 모든 부분집합
구하고자 하는 어떤 집합의 원소 개수가 n일 경우 부분집합의ㅣ 개수는 2^n이 나옴
'''
'''
백트래킹 기법으로 구하기
- 일반적인 백트래킹 접근방법 이용
- n 개의 원소가 들어있는 집합의 2^n개의 부분집합 만들떄
True False 값을 가지는 항목들로 구성된 n개의 리스트를 만드는 방법 이용
- 리스트의 ㄱ번째 항목은 ㄱ버째의 원소가 부분집합의 값인지 아닌지를 나타냄
'''


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


# 후보군을 구하는 함수
def construct_candidates(a,k,in_val,c):
    c[0] = True  # 출현하던지
    c[1] = False # 아니던지
    return 2 # 2가지 경우동안 for문 돌리기 위해


in_val = int(input()) # 구하고 싶은 부분집합 원소의 개수
# 3개의 원소로 이루어진 파워셋 구하기
MAXCANDIDATES = 100
NMAX = 100
a = [0] * NMAX
backtrack(a, 0, 3)

# 진행과정이 재귀구조이므로
# 젤 마지막에 호출된 경우가
'''
for i in range(ncandidates):
    a[k] = c[i]  # c[0] True
    backtrack(a, k, in_val)  # k = 1,2,3.., in_val = 3
'''
# i 가 0일 때 호출된 함수의
# 새로운 i = 0 ,1일 때를 다 돌고 오게 된다
# 따라서 부분집합 k=3이 되면
# i = 0일때 0111에서 ==> i = 1일때 0110
# 이전에 호출된 함수로 돌아와
# 이미 저장된 k = 1 인 상태로 오고  01/00 인 지점
# k=2, i = 0일때 010/0
# ==> k =3 , i=0 일 때 0101/ i = 1일때 0100 까지 돌고
# 다시 이전 함수로 돌아와 계속 반복
# k = 0인데로 오면 k= 일때 i =1 일때 부터 같은과정 반복 00/00
