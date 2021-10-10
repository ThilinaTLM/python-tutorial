

# 6,5,1,3,8,7,9,2
# 6,5,1,3               |   8,7,9,2
# 6,5  |  1,3       |       8,7    |    9,2

# 5,6  |  1,3  |  7,8  |  2,9
# 1,3,5,6      |  2,7,8,9
# 1,2,3,5,6,7,8,9


def merge(part1, part2):
    N1 = len(part1)
    N2 = len(part2)
    merged = []
    i = j = 0
    while True:
        if i >= N1:
            merged.extend(part2[j:])
            break
        elif j >= N2:
            merged.extend(part1[i:])
            break
        elif part1[i] < part2[j]:
            merged.append(part1[i])
            i += 1
        else:
            merged.append(part2[j])
            j += 1
    return merged


def merge_sort(values):
    N = len(values)
    if N <= 1:
        return values
    m = N//2
    part1 = values[0:m]
    part2 = values[m:]
    return merge(merge_sort(part1), merge_sort(part2))


values = [6, 5, 1, 3, 8, 7, 9, 2]
print(merge_sort(values))
