def fib(N, c ={0:0, 1:1}):
    if N in c:
        return(c[N])
    else:
        c[N] = fib(N-1,c) + fib(N-2,c)
        return c[N]
print(fib(int(input())))