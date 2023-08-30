# baby-gin
def is_trple(lst):
    if lst[0] == lst[1] and lst[1] == lst[2]:
        return True
    else:
        return False

def is_run(lst):
    if lst[0] == lst[1] - 1 and lst[1] == lst[2] - 1:
        return True
    else:
        return False

def perm(i, N, num):

    if i == N:  # 순열 완성
        # 만들어진 순열 p를 앞뒤 3개씩 잘라서 조사
        # run, triplet 조사
        f = [p[i] for i in range(3)]
        b = [p[i] for i in range(3,6)]
        if (is_run(f) or is_trple(f)) and (is_run(b) or is_trple(b)):
            print(f'baby-gin!! {f} {b}')
    else:
        for j in range(N):
            if used[j] == 0:
                p[i] = num[j]
                used[j] = 1
                perm(i + 1, N, num)
                used[j] = 0

num = [2, 3, 5, 7, 7, 7]
N = 6
p = [0] * 6
used = [0] * 6
perm(0, 6, [2, 3, 5, 7, 7, 7])
perm(0, 6, [1,2,3,4,5,6])
perm(0, 6, [2, 3, 4, 7, 7, 7])
perm(0, 6, [1, 7, 7, 7, 7, 7])