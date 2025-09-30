def triang(size,symb):
    i=0
    if int(size)%2==1:
        while i<=(int(size)-2)//2:
            print(str(symb)*(i+1))
            i+=1
        while i>=0:
            print(str(symb)*(i+1))
            i-=1
    else:
        i=1
        while i<=(int(size))/2:
            print(str(symb)*(i))
            i+=1
        while i>0:
            print(str(symb)*(i-1))
            i-=1
size,numb = input().split()
triang(size,numb)