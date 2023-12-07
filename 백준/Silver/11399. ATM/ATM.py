'''
각 사람이 돈을 인출하는데 필요한 시간은
앞 사람의 일출 시간에 영향을 받으므로
각 차례의 앞에는 자기보다 같거나 작은 수들만 있어야 한다
'''
import sys
input = sys.stdin.readline

N = int(input())
times = sorted(map(int, input().split()))

res = 0
for i in range(len(times)):
    res += times[i] * (len(times)-i)

print(res)