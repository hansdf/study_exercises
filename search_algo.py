# linear and binary search algorithms test on sorted lists

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def linear_find(numlist, target):
    pass
    

def binary_find(numlist, target):
    for n in range(1, len(numlist)):
        middle_n = int(len(numlist)/2) # index of middle element
        print("middlenum: ", middle_n)
        print("numlist[middle_n]: ", numlist[middle_n])
        if numlist[middle_n] == target:
            return print(f"found target: {target} at index: {numlist[middle_n]}")
        elif numlist[middle_n] < target:
            pass
        elif numlist[middle_n] > target:
            pass
        
        middle_n = middle_n/2

binary_find(nums,4)