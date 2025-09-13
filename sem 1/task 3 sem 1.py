a = input().split()
c=1
for i in range(len(a)):
    c*=int(a[i])
print(c**(1/len(a)))