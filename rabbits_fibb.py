def rabbits_fibb(n,m):
    dpArray=[0]*n
    dpArray[0]=1
    for i in range(1,n):
        if i<m:
            dpArray[i]=sum(dpArray[:i])
        else:
            dpArray[i]=sum(dpArray[i-m:i])

    return dpArray[-1]
n=6
m=3
result=rabbits_fibb
print(result)
