''''''
'''
## 수식 트리
    - 수식을 표현하는 이진 트리
    - 연산자는 루트 노드이거나 가지노드
    - 피연산자는 모두 잎 노드

## 이진 탐색 트리
- 탐색 연산
    - 루트에서 시작
    - 키값과 루트 노드의 키값 을 비교해서 같으면 탐색연산 성공
        - 키값 x < 루트노드의 키 값 : 루트노드의 왼쪽 서브트리에 대해 탐색연산
        - 키값 x > 루트노드의 키 값 : 루트노드의 오른쪽 서브트리에 대해 탐색연산
    - 서브트리에 대해서 순환적으로 탐색연산 반복
    
- 삽입 연산
    1. 먼저 탐색연산을 수행
        - 삽입할 원소가 트리에 있으면 삽입할 수 없으므로, 같은 원소가 트리에 있는지 탐색
        - 탐색 실패가 결정되는 위치가 삽입 위치
    2. 탐색 실패한 위치에 원소를 삽입한다.

- 삭제 연산
    
### 이진 탐색트리 - 성능
- 탐색, 삽입, 삭제 시간은 트리의 높이 만큼 시간이 걸린다
    - O(h), h: BST의 깊이(height)
- 평균의 경우
    - 이진 트리가 균형적으로 생성되어 있는 경우
    - O(log n)
- 최악의 경우
    - 한쪽으로 치우친 경사 이진트리의 경우
    - O(n)
    - 순차탐색과 시간복잡도가 같다.

- 검색 알고리즘의 비교
- 상용에서 검색을 위해 어떤 알고리즘?
    - 기본적으로 트리형태 혹은 해쉬
    
'''