def len_to_bin(len_s):
    
    # 길이 len_s 를 이진수로 변환
    res = bin(len_s)[2:]

    return res


def delete_zero(new_s,c):
    global cnt_zero
    
    arr = ''
    
    for i in range(c):
        if new_s[i] == '0':
            cnt_zero += 1
        else:
            arr += new_s[i]
    # 현재 이진수의 0 제외한 수 리턴
    
    return arr


def solution(s):
    answer = []
     
    cnt_zero = 0
    cnt = 0
    new_s = s
    while len(new_s) != 1: # s 가 1이 될 때까지
        now_s = ''
        
        for i in range(len(new_s)):
            if new_s[i] == '0':
                cnt_zero += 1
            else:
                now_s += new_s[i]
            
        new_s = len_to_bin(len(now_s))
        cnt += 1
    
    
    answer.append(cnt)
    answer.append(cnt_zero)
    
    return answer