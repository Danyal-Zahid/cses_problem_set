# https://cses.fi/problemset/task/1094

n = int(input())
numbers = list(map(int, input().split()))

ptr1 = 0
ptr2 = 1
increments = []
while ptr2 < n:
    if numbers[ptr1] > numbers[ptr2]:
        increments.append(numbers[ptr1] - numbers[ptr2])
    else:
        ptr1 = ptr2
    ptr2 += 1

print(sum(increments))