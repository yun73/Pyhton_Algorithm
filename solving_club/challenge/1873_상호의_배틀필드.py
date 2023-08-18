k = int(input())

# X 길이
# 1 > 2 0 11
# 2 > 4
# 4 > 8
X = '0'

while len(X) < 10**18:
    new_X = ''
    for i in X:
        i = (int(i) + 1)%2
        new_X += str(i)

    X = new_X + new_X[::-1]

print(X[k-1])