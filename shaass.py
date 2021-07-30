# https://codeforces.com/problemset/problem/294/A
n=int(input())
a=[int(i) for i in input().split(" ")]
m=int(input())
for i in range(m):
    line=input()
    x,y=int(line.split(" ")[0]),int(line.split(" ")[1])
    if(x>=1 and x<=n):
        a[x]=a[x]+y-1
    if(x>=1 and x<=n):   
        a[x-2]=a[x-2]+a[x-1]-y
    a[x-1]=0
for i in range(n):
    print(a[i])

