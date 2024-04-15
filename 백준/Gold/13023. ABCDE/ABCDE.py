import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def bt(cnt, now,visit):
    global res
    if cnt >= 4:
        res = 1
        return
    for next in near[now]:
        if next in visit:
            continue
        visit.add(next)
        bt(cnt+1,next,visit)
        visit.remove(next)


res = 0

N,M = map(int, input().split())

near = [[] for _ in range(N)]

for _ in range(M):
    a,b = map(int, input().split())
    near[b].append(a)
    near[a].append(b)


for i in range(N):
    visit = set()
    visit.add(i)
    # 현재 친구 부터 연관된 친구 쭉 탐색
    bt(0,i,visit)
    if res:
        break

print(res)