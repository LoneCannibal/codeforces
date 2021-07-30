# https://codeforces.com/problemset/problem/127/A
firstline=input().split(" ")
n,k=int(firstline[0]),int(firstline[1])
writing_speed=50
total_distance=0
for i in range(n):
    line=input()
    x2,y2=int(line.split(" ")[0]),int(line.split(" ")[1])
    if(i==0):
        x1,y1=x2,y2
    else:
        total_distance=total_distance+(((x2-x1)**2+(y2-y1)**2)**0.5)
        x1,y1=x2,y2
print(round(total_distance*k/writing_speed,9))