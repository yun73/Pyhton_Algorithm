# 1~9, 10~99 , 100 ~ 999

N = int(input())

l = len(str(N))

cnt = 0
for i in range(1,l):
    # 자릿수에 해당하는최대 다 저장
    cnt += 9 * 10**(i-1) * i
# 차이만큼 뺴주기
cnt += (N-10**(l-1) + 1) * l
print(cnt)
