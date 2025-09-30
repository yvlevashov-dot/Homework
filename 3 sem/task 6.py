x = list(map(int,input().split()))
y = list(map(int,input().split()))
def mnk(s1,s2):
    s1=0
    s2=0
    k=0
    b=0
    for i in range(len(x)):
        s1=s1+int(x[i])*int(y[i])
        s2=s2+int(x[i])**2
    s1=s1/len(x)
    s2=s2/len(x)
    k=(s1-(sum(x)/len(x))*(sum(y)/len(y)))/(s2-(sum(x)/len(x))**2)
    b = (sum(y)/len(y)) - k * (sum(x)/len(x))
    return k,b
print(mnk(x,y))