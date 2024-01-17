import sys
input = sys.stdin.readline

N = input().strip()
cnt = [0] * 10

for num in N:
    if num in '69':
        if cnt[6] >= cnt[9]:
            cnt[9] += 1
        else:
            cnt[6] += 1
        continue
    cnt[int(num)] += 1

print(max(cnt))