#with open( "text.txt") as f:
    #lines = f.readlines()
   # print(lines)
with open( "text.txt", "r") as f, open ("output.txt","w") as w:
    lines = f.readlines()
    numbers = list(map(int, lines[0].split()))
    op =lines[1].strip()
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
    w.write(str(res))