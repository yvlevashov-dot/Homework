a = input().split()
k=0
for i in a:
    if a.count(i)>a.count(k):
        k=i
print(k)