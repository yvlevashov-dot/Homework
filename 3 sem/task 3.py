a = int(input())
b=int(input())
def evc(a,b):
    a1=a
    b1=b
    while a!=0 and b!=0:
        if a>b:
            a =a%b
        else:
            b=b%a
    c=b+a
    x,y=1,1
    while x*a1+y*b1!=c:
        if x*a1+y*b1>c:
            x-=1
        if x*a1+y*b1<c:
            y+=1
    return (x,y,c)
print(evc(a,b))