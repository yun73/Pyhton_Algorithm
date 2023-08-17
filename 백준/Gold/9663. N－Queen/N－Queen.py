def gqueen(r, N, col, ld, rd):
    global possible
    if r == N:
        possible += 1
    else:
        for c in range(N):
            if (col[c] or ld[r - c + N - 1] or rd[r + c]):
                continue

            col[c] = ld[r - c + N - 1] = rd[r + c] = True
            gqueen(r + 1, N, col, ld, rd)
            col[c] = ld[r - c + N - 1] = rd[r + c] = False




N = int(input())
possible = 0

col = [False] * N
ld = [False] * (2 * N - 1)
rd = [False] * (2 * N - 1)

gqueen(0, N, col, ld, rd)
print(possible)