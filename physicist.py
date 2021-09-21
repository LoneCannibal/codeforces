#https://codeforces.com/problemset/problem/69/A
n=int(input())
x=[]
y=[]
z=[]
for i in range(n):
    temp=input().split(" ")
    x.append(int(temp[0]))
    y.append(int(temp[1]))
    z.append(int(temp[2]))
sumx,sumy,sumz=0,0,0
for i in range(n):
    sumx=sumx+x[i]
    sumy=sumy+y[i]
    sumz=sumz+z[i]
if(sumx+sumy+sumz==0):
    print("YES")
else:
    print("NO")