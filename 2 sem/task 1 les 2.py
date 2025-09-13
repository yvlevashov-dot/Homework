A=input().split()
n=int(A[0])
k=0
t=0
for i in A:
    k=int(i)^k
for p in range(n):
    t= t^p
print(k^t)