

# 6,5,1,3,8,7,9,2

# pivot 5
# 6,5,1,3,8,7,9,2

# pi = 6
# 5,1,3,2    | 8,7,9

# pi = 5            # pi = 8
# 1,3,2 |           # 7 | 9

# pi = 1
#     | 3,2


def quick_sort(values):
    N = len(values)
    if N <= 1:
        return values
    pi = values[0]
    part1 = []
    part2 = []
    for v in values[1:]:
        if v <= pi:
            part1.append(v)
        else:
            part2.append(v)
    return quick_sort(part1) + [pi] + quick_sort(part2)


values = [6, 5, 1, 3, 8, 7, 9, 2]
print(quick_sort(values))
