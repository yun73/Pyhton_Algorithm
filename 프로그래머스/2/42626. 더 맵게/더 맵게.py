import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    ans = 0
    while scoville[0] < K:
        # 만약 스코빌 길이가 1인데 그 값이 K 보다 작다면 -1 리턴
        if len(scoville) == 1:
            return -1
        mix = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville,mix)
        ans += 1

    return ans

