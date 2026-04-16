S = input().strip()
n = len(S)
if n == 0:
    print()

p = [0] * n
for i in range(1, n):
    k = p[i-1]
    while k > 0 and S[k] != S[i]:
        k = p[k-1]
    if S[k] == S[i]:
        k += 1
    p[i] = k

cnt = [1] * (n + 1) 
for i in range(n, 0, -1):
    cnt[p[i-1]] += cnt[i]
print(*cnt)