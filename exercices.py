def robbits_diff(n,m):
    rabbitsgeneration=[0]*m
    rabbitsgeneration[0]=1
    for month in range(1,n):
        newborns=sum(rabbitsgeneration[1:])
        for i in range(m-1,0,-1):
            rabbitsgeneration[i]=rabbitsgeneration[i-1]
        rabbitsgeneration[0]=newborns
    return sum(rabbitsgeneration)
n=88
m=20
result=robbits_diff(n,m)
print(result)

