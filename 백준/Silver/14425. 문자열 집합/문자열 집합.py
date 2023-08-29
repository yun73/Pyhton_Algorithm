# 문자열 집합
N, M = map(int, input().split())
S = set(input() for _ in range(N))

# 집합 S 에 포함된 문자열 개수
cnt = 0
# M 개의 문자열 입력받으며 집합 S에 있는지 확인
for _ in range(M):
    word = input()
    # 집합 S 안에 있는 단어이면
    if word in S:
        # 단어 개수 추가
        cnt += 1

print(cnt)