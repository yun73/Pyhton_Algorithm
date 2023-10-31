S = input()
suffix = []
for i in range(len(S)):
    # print(S[i:])
    suffix.append(S[i:])
suffix.sort()
for word in suffix:
    print(word)