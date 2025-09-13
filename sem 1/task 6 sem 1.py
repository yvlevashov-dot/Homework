with open( "task 6.txt", "r") as f, open ("output.txt","w") as w:
    A=[]
    lines = f.readlines()
    numbers = list(map(int, lines[0].split()))
    op =lines[1].strip()
    for i in numbers:
        a=0
        for k in range(len(str(i))):
            a+= int(str(i)[k]) *(int(lines[2])**(len(str(i))-k-1))
        numbers[numbers.index(i)] = a
    if op == "+":
        res = 0
        for i in numbers:
            res += i
    elif op == "*":
        res = 1
        for i in numbers:
            res *=i
    else:
        res = numbers[0]
        for i in range(1,len(numbers)):
            res -= numbers[i]
    while res != 0:
        A.append(res % int(lines[2]))
        res = res // int(lines[2])
    w.write(str(A[::-1]))