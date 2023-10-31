'''
LCS

LCS(Longest Common Subsequence, 최장 공통 부분 수열)

문자의 순서가 바뀌지 않는 가장 긴 공통 부분 수열을 구하는문제
- 비크마스킹으로 모든 겨웅를 하면 무조건 시간 초과
- python 으로 2초 대략 4천만번 계산 가능
- dp로 1000*1000 을 계산하면 100만 각 자리당 40번 까지 연산 가능하다 치자

- 가장 긴 부분수열부터 조사해야 한다.
- 첫 문자열의 처음 부분부터 조사할 때 부터 차례대로
dp[i][j] = i번째부터 시작했을 때의 최대 부분 수열 길이
앞에거에 영향을 받으면서 가자
'''

first = input()
second = input()
if len(first) <= len(second):
    short = first
    long = second
else:
    short = second
    long = first

dp = [[0]*len(long) for _ in range(len(short))]

for i in range(len(short)):
    if short[i] != long[0]:
        continue
    dp[i][0] = 1

for i in range(len(short)):
    for j in range(len(long)):
        dp[i][j] =

'''
      A C A Y K P
K     0 0 0 0 1 1  
AK    1 1 1 1 2 2
CAK   1 2 2 2 3 3
PCAK  1 2 2 2 3 3 
APCAK 2 3 4 4 4 4
CAPCAK2 3 4 4 4 4 
'''
