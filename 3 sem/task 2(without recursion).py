def div(N):
    res = []
    i=2
    while i<=N:
        if N%i==0:
            res.append(i)
            N=N//i
        else:
            i+=1
    return res
N=int(input())
print(div(N))