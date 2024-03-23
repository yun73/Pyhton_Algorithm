import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()
location = {}
for i in range(len(T)):
    location.setdefault(T[i],i)

arr = [0] * (len(T))
for word in S:
    if word not in location:
        continue
    if location[word] == 0:
        arr[location[word]] += 1
    else:
        if arr[location[word]-1] > 0:
            arr[location[word]-1] -= 1
            arr[location[word]] += 1

print(arr[-1])
