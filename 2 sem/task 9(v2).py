with open( "text.txt", "r") as f:
    lines = f.readlines()
count=0
s=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
s1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in lines:
    for j in range(len(i)):
        if (i[j]=="." or i[j]=="?" or i[j]=="!") and (i[j-1] in s1):
            count+=1
print(count)