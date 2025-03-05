def moveZeroes(nums): # move zeroes to the end of the list, keep rest of the list in same order.
        new_arr = []
        counter = 0
        for n in nums:
            if n != 0:
                new_arr.append(n)
            elif n == 0:
                counter += 1
                
        nums = new_arr
        for i in range(counter):
            nums.append(0)
        return nums


print(moveZeroes([0,1,2,5,0,11,0,222]))


