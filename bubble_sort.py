nums = [64, 34, 25, 12, 22, 11, 90]

def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                temp = nums[i - 1]
                nums[i - 1] = nums[i]
                nums[i] = temp
                swapping = True
                print(nums)
        end -= 1
    return nums

print(bubble_sort(nums))