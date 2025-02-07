# linear and binary search algorithms test on sorted lists

nums = [0, 1, 2, 15, 4, 5, 6, 7, 8, 9, 10]

def linear_find(numlist, target): # iterate entire list
    index = 0
    for n in numlist:
        if n == target:
            print("found target at index", index)
        index += 1
    

def binary_find(numlist, target):
    first_item = 0
    last_item = len(numlist) - 1

    for n in range(1, len(numlist)):
        middle_n = len(numlist) // 2 # index of middle element

        if numlist[middle_n] == target:
            return print(f"found target: {target} at index: {numlist[middle_n]}")
        elif numlist[middle_n] < target:
            print(f"Queried number {numlist[middle_n]} is smaller than target")
            middle_n = int(middle_n/2) # update index to check in next iteration
            print("new middle_n is: ", middle_n)
        elif numlist[middle_n] > target:
            print(f"Queried number {numlist[middle_n]} is bigger than target")
            middle_n = int(middle_n/2) # update index to check in next iteration
            print("new middle_n is: ", middle_n)
        
        
# binary_find(nums, 9)

linear_find(nums, 15)