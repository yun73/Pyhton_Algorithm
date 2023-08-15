# arr = list(map(int,input()))
# print(arr)
# s = input()
# print(s[1])
# s[1] = 4
# print(s[1])


# s = 'Reverve'
# s_list = list(s)
# N = len(s)
# print(N)
# for i in range(N//2):
#     s_list[i], s_list[N-1-i] = s_list[N-1-i], s_list[i]
# print(s_list)
# s = ''.join(s_list)
# print(s)
#
# s1 = 'abc'
# s2 = 'abc'
# s3 = 'def'
# s4 = s1
# s5 = s1[:2] +'c'
# print(s1, s2, s5)
# if s1 == s5:
#     print('s1==s5')
# else:
#     print('s1!=s5')
# if s1 is s5:
#     print('s1 is s5')
# else:
#     print('s1 is not s5')
#
# if s1 == s2:
#     print('s1==s2')
# else:
#     print('s1!=s2')
# if s1 is s2:
#     print('s1 is s2')
# else:
#     print('s1 is not s2')
#
# if s5 == s4:
#     print('s5==s4')
# else:
#     print('s5!=s2')
# if s5 is s4:
#     print('s5 is s4')
# else:
#     print('s5 is not s4')

# s1 = 'abc'
# s2 = 'abC'
# print(s1<s2)
# print(s2<s1)
# print(s1==s2)

def itoa(a):
    s = ''
    while a>0:
        s += chr(ord('0') + a % 10) # 1의 자리 숫자의 ascii값 알아냄
        a //= 10

    return s[::-1]

a= 123
print(itoa(a))

