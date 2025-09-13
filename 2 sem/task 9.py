with open( "text.txt", "r") as f:
    lines = f.readlines()
count=0
s=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for i in lines:
    for j in i:
        if j in s:
            count+=1
print(count)