n = int(input())

cnt_n , cnt_before = 1, 0

for i in range(n):
    cnt_n, cnt_before = (cnt_n + cnt_before)%10, cnt_n%10

print(cnt_n)