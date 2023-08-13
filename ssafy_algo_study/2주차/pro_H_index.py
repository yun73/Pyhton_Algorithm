# H-Index는 과학자의 생산성과 영향력을 나타내는 지표
# 논문 n편 중, h번 이상 인용된 논문이
# h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index
# 논문 인용횟수 h 인 논문 개수가 h보다 크고
# 나머지 논문이 h보다 작으면면

# citations 은 리스트로 주어지는 입력값
# [3, 0, 6, 1, 5]
# [6,5,3,1,0]
# 인용횟수 최대 10000
# 논문의 수는 주어지는 배열 크기

def solution(citations):
    # 먼저 citation 정렬하기
    citations.sort(reverse=True)  # 버블?, 카운팅?, 선택?
    N = len(citations)
    # 앞서 부터 세면서 반복돌 떄마다 1씩 증가해서 이게 행당 논문 이용된 수랑 같은지 비교
    # 아니면 앞에서 부터 하면서 해당 인덱스 값을 이용해 비교
    max_c = 0
    for i in range(N):
        if citations[i] >= (i + 1):
            max_c = i + 1

    return max_c

