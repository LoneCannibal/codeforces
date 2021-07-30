# https://codeforces.com/problemset/problem/424/A
n=int(input())
hamster=input()
smallx,bigx=0,0
for i in hamster:
    if(i=='x'):
        smallx=smallx+1
    else:
        bigx=bigx+1
print(int(abs(smallx-bigx)/2))
if(smallx>bigx):
    for i in range(len(hamster)):
        if(hamster[i]=='x' and smallx!=bigx):
            print("X", end = '')
            smallx=smallx-1
            bigx=bigx+1
        else:
            print(hamster[i], end = '')
elif(bigx>smallx):
    for i in range(len(hamster)):
        if(hamster[i]=='X' and smallx!=bigx):
            print("x", end = '')
            bigx=bigx-1
            smallx=smallx+1
        else:
            print(hamster[i], end = '')
elif(bigx==smallx):
    print(hamster)