number_of_values = input()
values = input().split()
distinct_values = 0
_map = {}
for i in values:
    val = _map.get(i, None)
    if val is None:
        _map[i] = 1
        distinct_values += 1

print(distinct_values)