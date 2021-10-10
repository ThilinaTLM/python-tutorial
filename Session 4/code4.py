

lst = [2, 5, 1, 10, 22]
# print(sum(lst))


def total(values):
    if not values:
        return 0
    if len(values) == 1:
        return values[0]
    return values[0] + total(values[1:])


# print(total(lst))


# Searching

def search(lst, v):
    for i in lst:
        if i == v:
            return True
    return False

# values, v -> True | False


def r_search(values, v):
    if not values:
        return False
    if values[0] == v:
        return True
    return search(values[1:], v)


print(r_search(lst, 13))


# palindrome
# 1221, abba, aba, a

# palindrome -> True | False
def is_palindrome(s):
    if len(s) < 2:
        return True
    return (s[0] == s[-1]) and is_palindrome(s[1:-1])


print(is_palindrome('bbcdcba'))
