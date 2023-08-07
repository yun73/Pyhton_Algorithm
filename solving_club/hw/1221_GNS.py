T = int(input())
for tc in range(1, T+1):
    t, N = input().split()
    strings = list(input().split())
    str_num = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    # print(strings)
    count = [0] * 10
    # N = len(strings)
    # print(N)
    # N2 = (int(length)+1)//4
    # print(N2)
    # 정렬할 리스트
    arr = [''] * int(N)
    # 리스트의 인덱스 번호가 문자가 가르키는 숫자
    # 입력받은 문자열들을 딕셔너리에서 찾아 그 값에 해당하는 인덱스를 이용하여 카운트
    for i in range(int(N)):
        count[str_num[strings[i]]] += 1

    for i in range(9):
        count[i+1] += count[i]

    for i in range(int(N)-1,-1,-1):
        count[str_num[strings[i]]] -= 1
        arr[count[str_num[strings[i]]]] = strings[i]

    print(t)
    print(' '.join(arr))