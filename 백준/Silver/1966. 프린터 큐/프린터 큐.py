'''
조건에 따라 인쇄하는 프린터기

1. 현재 Queue의 가장 앞 문서의 '중요도' 확인
2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면
    >> 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다.
    그렇지 않다면
    >> 바로 인쇄를 한다.

입력
N : 1 ~ 100
M : 0 ~ N
중요도 : 1 ~ 9

'''
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split()) # N : 문서의 개수, M : 궁금한 문서가 몇번째에 놓여 있는지
    importance = list(map(int, input().split())) # N 개 문서의 중요도
    arr = []
    check = {}
    for i in range(1,10):
        check.setdefault(i,0)

    for idx,weight in enumerate(importance):
        arr.append((idx,weight))
        check[weight] += 1



    cnt = 0
    while True:
        for i in range(9,arr[0][1],-1):
            if check[i] > 0: # 현재 문서보다 중요도 높은게 하나라도 있으면
                arr.append(arr.pop(0)) # 큐 뒤로 보내기
                break
        else: # 중요도 높은게 하나도 없었다면
            check[arr[0][1]] -= 1 # 현재 문서 중요도 개수 1 줄여주고 프린트
            print_docs = arr.pop(0)
            cnt += 1 # 출력한 문서 개수 1 증가
            # 만약 출력한 문서가 M 번째 문서라면 종료
            if print_docs[0] == M:
                break

    print(cnt)