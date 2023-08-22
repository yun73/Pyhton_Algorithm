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


# 규훈이 형 풀이
T = int(input())

for tc in range(1, T + 1):
    memory = list(map(int, input()))

    # 초기상태 제공
    zero_bit = list([0] * len(memory))
    cnt = 0
    for bit in range(len(memory)):
        if memory[bit] != zero_bit[bit]:
            val = bit
            # 0이라면 1로, 1이라면 0으로 끝까지 변환
            if zero_bit[bit] == 0:
                while val < len(memory):
                    zero_bit[val] = 1
                    val += 1
            else:
                while val < len(memory):
                    zero_bit[val] = 0
                    val += 1
            cnt += 1

    print(f'#{tc} {cnt}')

# 홍찬이형 풀이
def swea1289():
    for tc in range(1, int(input()) + 1):
        bitbit = input()
        ans = int(bitbit[0])
        bb = bitbit[0]
        for b in bitbit[1:]:
            if bb != b:
                ans += 1
                bb = b

        print(f"#{tc} {ans}")


if __name__ == "__main__":
    swea1289()