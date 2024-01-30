# https://cses.fi/problemset/submit/1070/

def print_numbers(start, end):
    while start <= end:
        print(start, end=" ")
        start += 2

n = int(input())

if 2 <= n < 4:
    print("NO SOLUTION")
else:
    print_numbers(2, n)
    print_numbers(1, n)

