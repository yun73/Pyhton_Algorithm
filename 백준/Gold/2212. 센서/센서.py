# 센서
# 고속도로 위에 N 개의 센서, 이를  수집할 집중국 최대 K 개
# 센서가 적어도 하나의 집중국과는 통신이 가능해야 한다.

# 센서의 개수
N = int(input())
# 집중국의 개수
K = int(input())

# 센서좌표 N 개 : 센서들은 직선위의 한 기점인 원점으로부터 정수 거리에 위치
location = list(map(int, input().split()))
# 집중국이 수신 가능한 영역의 길이 = 각 영역의 끝 - 시작
location.sort()
# 만약 위치가 하나 뿐이라면
# 앞에서 부터 집중국 세울 건지 정하고
# 각 위치에서 앞의 좌표와의 거리 구한 리스트
dis = [0]*(N-1)
for i in range(1,N):
    dis[i-1] = location[i] - location[i-1]

# K개의 집중국을 설치하려면 현재 가지고 있는 거리 리스트에서 K-1 개를 없애줘야해
# 없애주는 곳은 거리가 최대인 곳들부터 차례로
dis.sort()

# 최소거리
result = 0
for i in range(N-K):
    result += dis[i]

print(result)