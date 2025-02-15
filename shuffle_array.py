# Leetcode 1470. Shuffle the Array
# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

nums = [2,5,1,3,4,7]
n = 3
# Expected output: [2,3,5,4,1,7] 

def shuffle_array(nums,n):
    list_start = 0
    second_list_start = n
    shuffled_list = []
    nums = nums*2
    for num in range(n):
        shuffled_list.append(nums[list_start])
        shuffled_list.append(nums[second_list_start])
        list_start+=1
        second_list_start+=1
    
    print(shuffled_list)


shuffle_array(nums,n)