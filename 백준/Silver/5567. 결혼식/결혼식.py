import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
friends = [[] for _ in range(N+1)]
set_friends = set()

for _ in range(M):
    a,b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)

for first in friends[1]:
    set_friends.add(first)
    for second in friends[first]:
        if second != 1 and second not in set_friends:
            set_friends.add(second)

print(len(list(set_friends)))
