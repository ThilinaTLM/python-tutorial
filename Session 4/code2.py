

values = [5, 3, 10, 8, 20, 9]


def bubble_sort(nums):
    repeat = True
    while repeat:
        repeat = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                repeat = True
    return nums


print(values)
bubble_sort(values)
print(values)
