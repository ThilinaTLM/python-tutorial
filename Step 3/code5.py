
# 
def sort_numbers(input_list):
    nums = list(input_list)
    check = True
    while check:
        check = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                check = True
    return nums

# 
def sort_string_by_last_char(input_list):
    nums = list(input_list)
    check = True
    while check:
        check = False
        for i in range(len(nums) - 1):
            if nums[i].lower()[-1] > nums[i+1].lower()[-1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                check = True
    return nums

def sort_key_last_char(word):
    return word.lower()[-1]

def sort_key_abs(num):
    return abs(num)


words = ['Mala', 'Jacob', 'AamA']
# sorted_words_by_last_char = sort_string_by_last_char(words)
# print(sorted_words_by_last_char)

# words.sort(key=sort_key_last_char)
# print(words)

# nums = [10, 2, 48, 1, 15] # mutable
# sorted_nums = sort_numbers(nums)
# print(nums)
# print(sorted_nums)


# nums = [10, 2, -48, 1, 15] # mutable

# nums.sort(key=lambda x: abs(x))
# nums.sort(key=sort_key_abs)
# print(nums)