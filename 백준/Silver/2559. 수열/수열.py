'''
IM 대비 문제 풀기
'''
# 수열
# N 온도 측정 일수, K 합할 연속 일수
N, K = map(int, input().split())
# 온도 데이터
temp = list(map(int, input().split()))
K_sum = []
# 처음 K일의 합을 미리 구하여 다음 합에 이용
K_sum.append(sum(temp[:K]))
for i in range(N-K):
    # 순회가 진행 될 때 마다 K_sum의 top이 i = 0, top = 0 ==> i = 1, top = 1
    # 이전 K일 동안의 합에 시작온도 빼고 하루 뒤의 온도 추가
    K_sum.append(K_sum[i] - temp[i] + temp[K+i])

print(max(K_sum))


