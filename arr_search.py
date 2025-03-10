# First and last index in sorted array

nlist = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]

def find_first(nums,target):
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            if nums[mid-1] == target:
                right = mid - 1
            else:
                return mid
        elif nums[mid] > target:
            right = mid -1 
        elif nums[mid] < target:
            left = mid + 1

def find_last(nums,target):
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            if nums[mid+1] == target:
                right = mid + 1
            else:
                return mid
        elif nums[mid] > target:
            right = mid -1 
        elif nums[mid] < target:
            left = mid + 1

def first_and_last(nums,target):
    ret_arr = []
    ret_arr.append(find_first(nums,target))
    ret_arr.append(find_last(nums,target))
    print(ret_arr)
        
first_and_last(nlist, 5)

