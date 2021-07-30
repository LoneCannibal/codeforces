# https://codeforces.com/problemset/problem/467/A
n=int(input())
number_of_rooms=0
for i in range(n):
    lines=input().split(" ")
    p,q=int(lines[0]),int(lines[1])
    if(q-p>=2):
        number_of_rooms=number_of_rooms+1
print(number_of_rooms)