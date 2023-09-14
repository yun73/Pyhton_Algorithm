# 잃어버린 괄호
# 괄호를 쳐서 식의 값을 최소로 만들자
# 문제 조건상 (숫자 연산자 숫자) 형태로만 묶을 수 있
def bt(r,susik,result,o,c):
    global min_value

    if r == len(susik):
        if o == c: # 괄호가 올바르게 생겼을 때
            value = eval(result)
            if min_value > value:
                min_value = value
        else:
            result +=')'*(o-c)
            value = eval(result)
            if min_value > value:
                min_value = value
        return
    else:
        # 연산자가 아니면 즉 숫자가 나오면 괄호 추가
        if susik[r] not in '+-':
            bt(r+1,susik,result+'('+susik[r],o+1,c)
            if o>c: # 현재 여는 괄호가 닫는 괄호보다 많으면
                bt(r + 1, susik, result + susik[r]+')', o, c+1)
        # 연산자가 나오면 괄호 닫거나
        else:
            bt(r+1,susik,result+str(susik[r]),o,c)


sik = input()
susik = []
i = 0
stack = ''
while i < len(sik):
    # 종료 조건 만약 수식의 모든 요소를 다 사용했으면
    if sik[i] not in '-+': # 숫자이면
        stack += sik[i]
        if i == len(sik)-1:
            susik.append(str(int(stack)))
        i += 1
    else: # 연산자이면
        if stack != '':
            susik.append(str(int(stack)))
        stack = ''
        susik.append(sik[i])
        i+=1

min_value = eval(''.join(susik))
# print(susik)
o = 0 #현재 들어가 있는 여는 괄호
c = 0 # 현재 들어가 이쓴ㄴ  닫는 괄호
bt(0,susik,'',o,c)
print(min_value)
# 맨 앞에서 부터 '(' 괄호를 넣고 시작
# ( 들어갈 수 있는 곳 : 숫자 앞 = 연산자 뒤
# ) 들어갈 수 있는 곳 : 숫자 뒤 = 연산자 앞



