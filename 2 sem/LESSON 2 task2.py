a , b = input().split()
c=str()
for i in range(int(len(b)/int(a))):
    c+=b[i*int(a):(i+1)*int(a)][::-1]
print(c)