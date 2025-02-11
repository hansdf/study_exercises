#You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
#Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

nums = [-1,0,2,4,6,8,10,12,15,20,22,27]
target = 6

def binary_search(numlist, target):
    left = 0
    right = len(numlist)-1
    print(f"The passed array has {len(numlist)} elements, starting with left index: {left} and ending in index: {right}")
    while left <= right:
        middle = (left+right) // 2
        # print(middle)
        if numlist[middle] == target:
            print("found target at index:", middle)
            return middle
        elif target > numlist[middle]:
            print("target is bigger than item in the middle index")
            left = middle+1
            print(f"new resized list goes from {left} to {right}")
        elif target < numlist[middle]:
            print("target is smaller than item in the middle index")
            right = middle-1
            print(f"new resized list goes from {left} to {right}")



binary_search(nums, target)