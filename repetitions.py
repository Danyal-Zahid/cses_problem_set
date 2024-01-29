# https://cses.fi/problemset/task/1069

sequence = input()

ptr1 = 0
ptr2 = 0
max_rept = 0
running_rept = 0
while ptr2 < len(sequence): 
    if sequence[ptr1] == sequence[ptr2]:
        running_rept += 1
        ptr2 += 1
    else:
        ptr1 = ptr2
        if max_rept < running_rept:
            max_rept = running_rept
        running_rept = 0

if max_rept < running_rept:
    max_rept = running_rept
        

print(max_rept)
