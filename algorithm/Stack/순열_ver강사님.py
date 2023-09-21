numbers = [1,2,3,4,5]

n = len(numbers)

# i 번째 원소의 자리를 바꿔가면서 순열 생성
# 자리를 바꿀수 있는 경우의 수
def perm1(i):

    # 종료조건
    if i == n:
        print(numbers)
        return
    # 재귀호출
    # 현재위치 i에서 다른위치 j에 있는 숫자와 자리를 바꾼다
    # j를 선택할 때는 중복을 방지하기 위해 i보다 뒤에 있는 원소만 선택
    # i,j가 같을 수도 있다. (자리 안바꾸는 경우)
    # i 번째 원소를 누구랑 바꿀지 정했다면 i +1 번째 원소를 바꾸러 진행

    for j in range(i, n):
        # i 번째와 j 번째 위치를 바꾸고 진행
        numbers[i], numbers[j] = numbers[j], numbers[i]
        # 다음 i+1 번째 원소의 자리를 바꿀 간다
        perm1(i+1)
        # i 번째와 j 번째 원소를 되돌리고 진행
        numbers[i], numbers[j] = numbers[j], numbers[i]

# perm1(0)



numbers = [1,2,3,4,5]
n = len(numbers)
# 순열의 i번째 자리를 누구로 할것인가 직접 선택하는 방법
# i 번째 자리를 누구로 선택했는지 기억해야 중복선택 xx

# selected[i] == 1 : i 번째 위치에 사용한 원소 . selected 가 순열
# selected[]

def perm2(i, selected):

    # 종료 조건
    if i == n:
        print(selected)
        return

    # 재귀호출
    # 현재 위치 i에 누구를 놓을것인가 선택
    # 이전에 선택했던 원소는 선택 xx
    for j in range(n):
        # j 번쨰 원소를 선택한적이 없다면 j번째 원소를 순열의 i에 놓기
        if numbers[j] not in selected:
            # i번째 위치에 j원소 놓기
            selected[i] = numbers[j]
            # i번째 위치에 누굴 놓으지 정했으니 i+1 번째에 누굴 놓을지 정하러 가기
            perm2(i+1, selected)
            # i 번째 위치에 j를 놓았던거 없던일로 하고 다른 j를 선택하러
            selected[i] = 0


perm2(0, [0] *5)