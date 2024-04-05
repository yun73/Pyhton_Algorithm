def solution(s):  
    cnt_zero = 0
    cnt = 0
    new_s = s
    while len(new_s) != 1: # s 가 1이 될 때까지

        num = new_s.count('0')
        cnt_zero += num
        new_s = bin(len(new_s)-num)[2:]
        cnt += 1
    
    return cnt,cnt_zero