# https://codeforces.com/problemset/problem/540/A
n=int(input())
firstline,secondline=input(),input()
current_combination=[int(i) for i in firstline]
correct_combination=[int(i) for i in secondline]
total_turns=0
for i in range(n):
    turns=abs(current_combination[i]-correct_combination[i])
    if(turns>=5):
        total_turns=total_turns+(10-turns)
    else:
        total_turns=total_turns+turns
print(total_turns)