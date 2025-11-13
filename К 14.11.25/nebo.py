N = list(map(int,input().split()))
N1 = [-1]
ptp = [[0,N[0]]]
for i in range(1,len(N)):
    if N[i] > ptp[-1][1]:
        ptp.append([i,N[i]])
        N1.append(-1)
    else:
        for j in range(i-1,ptp[-1][0]-1,-1):
            if N[j] > N[i] or N[j] == N[i]:
                #print(i-1,ptp[-1][0])
                N1.append(j)
                break
            elif N[j] < N[i]:
                pass
print(*N1)