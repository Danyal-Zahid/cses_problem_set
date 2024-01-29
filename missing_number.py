# https://cses.fi/problemset/task/1083

n = int(input())
numbers = list(map(int, input().split()))
_sum = (n*(n+1)) / 2
_missing_sum = sum(numbers)
print(int(_sum - _missing_sum))
