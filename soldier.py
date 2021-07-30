# https://codeforces.com/problemset/problem/546/A
firstline=input().split(" ")
k,n,w=int(firstline[0]),int(firstline[1]),int(firstline[2])
total_price=0
for i in range(1,w+1):
    total_price=total_price+i*k
if(n>=total_price):
    print("0")
else:
    print(total_price-n)