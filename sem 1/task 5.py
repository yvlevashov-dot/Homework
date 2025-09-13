N = input()
b=int(input())
c=int(input())
t=int(0)
for i in range(len(N)):
    t= t +int(int(N[i])*(b**(len(N)-i-1)))
A=[]
while t!=0:
    A.append(t%c)
    t=t//c
print(A[::-1])