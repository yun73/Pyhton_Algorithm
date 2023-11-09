N,B = input().split()
B = int(B)

num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = {}
for i in range(len(num)):
    number[num[i]] = i

res = 0
for i in range(len(N)):
    res += number[N[i]]*(B**(len(N)-i-1))

print(res)