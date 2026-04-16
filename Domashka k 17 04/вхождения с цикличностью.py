def z_function(S):
    zf = [0] * len(S)
    left, right = 0,0
    for i in range(1, len(S)):
        zf[i] = max(0,min(zf[i-left], right - i))
        while i + zf[i] < len(S) and S[zf[i]] == S[i + zf[i]]:
            zf[i] += 1
        if i + zf[i] > right:
            left,right = i, i + zf[i]
    return zf

#Функция поиск подстроки в строке(Алгоритм Кнута - Мориса - Пратта)
def find(S,T):
    SS = S + "#" + T
    zf = z_function(SS)
    result = list()
    for i in range(len(zf)):
        if zf[i] == len(S):
            result.append(i - len(S))
    return(result)

S,T = input(), input()
Var_S = [S]
for i in range(len(S)-1):
    T1 = S[i + 1:] + S[:i + 1]
    Var_S.append(T1)
count = 0
for i in Var_S:
    print(i,find(i,T))
    count += len(find(i,T))
print(count)