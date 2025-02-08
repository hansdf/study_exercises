# Given an integer array nums and an integer val, remove all occurrences of val in nums. Then return the number of elements in nums which are not equal to val.

def remove_element(nums, val):
    index = 0
    for n in nums:
        #print("n: ", n)
        if n == val:
            nums[index] = 99
        index += 1
    
    print("after replace - nums: ", nums)
    
    not_val_counter = 0
    for j in nums:
        print("j: ", j)
        if j != 99:
            not_val_counter += 1
    print(not_val_counter)

numberslist = [0,1,2,2,3,0,4,2]
remove_element(numberslist, 2)