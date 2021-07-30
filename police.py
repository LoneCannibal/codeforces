# https://codeforces.com/problemset/problem/427/A
n=int(input())
police_force=0
unsolved_cases=0
activity=input().split(" ")
for i in range(n):
    if(int(activity[i])!=-1):
        police_force=police_force+int(activity[i])
    else:
        if(police_force==0):
            unsolved_cases=unsolved_cases+1
        else:
            police_force=police_force-1
print(unsolved_cases)