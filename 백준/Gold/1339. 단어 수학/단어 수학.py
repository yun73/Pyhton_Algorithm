'''
단어 수학문제

N 개의 단어 대문자로만
알파벳 대문자를 0 부터 9 까지 숫자중 하나로 바꿔서 N 개의 수를 합하는 문제
같은 알파벳을 같은 숫자, 2개 이상 알파벳이 같은 숫자로 바뀌면 안됨

수의 합을 최대로 만들기

'''





N = int(input())
number = []
word_num = {}
for i in range(N):
    word = input()
    for alpha in word:
        word_num.setdefault(alpha,0)

    word_8 = ''
    for j in range(0,8-len(word)):
        word_8 +='0'
    word_8 += word
    number.append(word_8)

for c in range(8):
    for r in range(N):
        if number[r][c] == '0':
            continue
        word_num[number[r][c]] += 10**(7-c)

numbers = list(word_num.values())
numbers.sort(reverse=True)
total = 0
can_use = 9
for num in numbers:
    total += num * can_use
    can_use -= 1

print(total)