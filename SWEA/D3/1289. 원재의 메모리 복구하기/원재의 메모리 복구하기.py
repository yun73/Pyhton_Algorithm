# 원재의 메모리 복구하기
T = int(input())
for tc in range(1, T+1):
    memory = list(map(int, input()))
    m = len(memory)
    now = [0] * m
    count = 0
    if memory[0] == 1:
        count += 1
    for i in range(1,m):
        if memory[i] != memory[i-1]:
            count += 1

    print(f'#{tc} {count}')