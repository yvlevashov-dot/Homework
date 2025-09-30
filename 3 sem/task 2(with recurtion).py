def div(n, i=2):
    while(i*i<=n):
        if n%i != 0:
            i+=1
        else:
            return [i] + div(n//i, i)
    return [n]
print(div(n=int(input())))