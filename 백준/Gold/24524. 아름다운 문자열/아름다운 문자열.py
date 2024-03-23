S = input()
t = input()
dp = [0]*(len(t)+1)
dp[0] = int(1e9)
t_idx = {a:idx+1 for idx,a in enumerate(t)}

for word in S:
    if word in t_idx and dp[t_idx[word]-1] > dp[t_idx[word]]:
        dp[t_idx[word]] += 1

print(dp[-1])
