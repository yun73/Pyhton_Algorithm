a = int(input())
b = input()
total = 0
for i in range(len(b)):
    sub_total = a*int(b[-1-i])
    total += sub_total*(10**i)
    print(sub_total)
print(total)