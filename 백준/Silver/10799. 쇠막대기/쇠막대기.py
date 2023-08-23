# 쇠막대기
all = input()
steel = []  # 쇠막대기의 스택
# 쇠막대기 조각
piece = 0
for i in range(len(all)):
    # 입력된 괄호들을 하나씩 받아오며 여는 괄호이면 스택에 저장
    if all[i] == '(':
        steel.append('(')
    # 만약 열린괄호 바로 뒤에 닫는 괄호가 오면
    else:  # 나온 값이 ')' 일때
        if all[i - 1] == '(':  # 만약 닫는 괄호 앞에 열린괄호가 있으면
            # pop()으로 괄호를 하나 가져오고 레이저가 발사
            steel.pop()
            # 그때 steel에 남아있는 수만큼 조각이 생김
            piece += len(steel)
        else:  # 만약 닫는 괄호 앞에 닫는괄호가 있으면
            steel.pop()  # 그 괄호는 쇠막대기 하나가 사라진다는 얘기기
            # 그러면 스택에서 쇠막대기 하나를 빼준다
            # 그리고 막대기의 잘린 끝부분 한개 추가'
            piece += 1

print(piece)