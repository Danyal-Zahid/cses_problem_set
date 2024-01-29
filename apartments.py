# https://cses.fi/problemset/task/1084

applicants, free, dif = list(map(int, input().split()))
desired_sizes = list(map(int, input().split()))
sizes = list(map(int, input().split()))

desired_sizes.sort()
sizes.sort()

opt = 0
free_apartment = 0
for applicant in range(applicants):
    desired_size = desired_sizes[applicant]
    while free_apartment < free:
        apartment_size = sizes[free_apartment]
        lower_limit = desired_size - dif
        upper_limit = desired_size + dif
        if lower_limit <= apartment_size <= upper_limit:
            opt += 1
            free_apartment += 1
            break
        if apartment_size >= lower_limit:
            break
        free_apartment += 1

print(opt)