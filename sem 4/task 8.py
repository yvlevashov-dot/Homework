a=[1,2,3,4,5,6,7]
b=[3,4,6,8,9,10,11]
s=set()
s3={1,2,3,4,5,6,7}
s4={3,4,6,8,9,10,11}
s1=[]
s2=[]
for i in a:
    s.add(i)
for i in b:
    s.add(i)
for i in a:
    if i not in b:
        s1.append(i)
for i in b:
    if i not in a:
        s2.append(i)
print("Уникальные 1", s1)
print("Уникальные 2", s2)
print("Уникальные объединения", s)
print("общие", ((s.intersection(s3)).intersection(s4)))