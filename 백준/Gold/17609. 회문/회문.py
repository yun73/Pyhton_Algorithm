# 40분 런타임에러
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def palin(l,r):
    global delete_cnt
    global possible

    if l > r:
        return

    if s[l] == s[r]:
        palin(l+1,r-1)
    else:
        # 오른쪽 문자 제거
        if s[l] == s[r - 1]:
            tmp = s[l:r]
            if tmp[:] == tmp[::-1]:
                possible = True
                delete_cnt = 1
                return
        # 왼쪽 문자 제거
        if s[l + 1] == s[r]:
            temp = s[l + 1:r + 1]
            if temp[:] == temp[::-1]:
                possible = True
                delete_cnt = 1
                return
        # 회문 아니면 2
        delete_cnt = 2
        return



T = int(input())
for tc in range(1,T+1):
    s = input().rstrip()
    l,r = 0,len(s)-1
    possible = False
    delete_cnt = 1
    if s == s[::-1]:  # 바로 회문인 경우
        print(0)
    else:
        palin(l,r)
        if possible:
            print(delete_cnt)
        else:
            print(2)

