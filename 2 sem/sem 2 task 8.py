n=int(input())
N=input().split()
for a in N:
    c=0
    for i in N:
        if a>i:
            c+=1
    if c==(n)//2:
        print(a)
        break