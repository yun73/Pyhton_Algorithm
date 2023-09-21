def f(i, N):
    if  i ==N:
        print(bit , end = ' ')
        for j in range(N):
            if bit[j]:
                print(A[j], end =' ')
        print()
        return
    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)


A = [1,2,3]
bit = [0] *3
f(3,3)