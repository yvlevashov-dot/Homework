S=["A", "H", "I", "M", "O", "T", "U", "V", "W", "X", "Y", "1", "8", "E", "J", "S", "Z"]
S1=["A", "H", "I", "M", "O", "T", "U", "V", "W", "X", "Y", "1", "8", "3", "L", "2", "5"]
a = list(input())
if a==a[::-1]:
    c=2
    for i in range(len(a)//2+1):
        if (a[i] in S or a[i] in S1) and (a[(-1)*i-1] in S or a[(-1)*i-1] in S1):
            if S.index(a[i])==S1.index(a[(-1)*i-1]):
                c=2
            if S.index(a[i])!=S1.index(a[(-1)*i-1]):
                print(a, "is a reg pol")
                c=0
                break
        else:
            c=0
            print(a, "is a reg pol")
            break
    if c==2:
        print(a, "is a mir pol")
else:
    c1=2
    for i in range(len(a)//2+1):
        if (a[i] in S or a[i] in S1) and (a[(-1)*i-1] in S or a[(-1)*i-1] in S1):
            if S.index(a[i])==S1.index(a[(-1)*i-1]):
                c1=2
            if S.index(a[i])!=S1.index(a[(-1)*i-1]):
                print(a, "is not a pol")
                c1=0
                break
        else:
            c1=0
            print(a, "is not a pol")
            break
    if c1==2:
        print(a, "is a mirror str")