n=int(input())
square=0
for i in range(1,n+1):
    for j in range(i,n//i+1):
        square+=1
print(square)