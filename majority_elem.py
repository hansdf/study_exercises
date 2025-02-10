# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

nums = [2,2,1,1,1,2,2,3,3,3,3,3,3,2,2,2,2,2]

def find_maj_elem(lst):
    # start a hashmap to store number of appearances of each number
    hash_counter = {}

    # iterate through list and store numbers and quantity of each in a hashmap
    for n in nums:
        if n not in hash_counter:
            hash_counter[n] = 1
        else:
            hash_counter[n] += 1

    # initiate counter var to store highest in hashmap
    highest_value_so_far = 0
    highest_key_so_far = 0

    # iterate through hashmap and compare each value against counter, if higher, replace counter with it
    for key in hash_counter:
        print(key, "->", hash_counter[key] )
        if hash_counter[key] > highest_value_so_far:
            highest_value_so_far = hash_counter[key]
            highest_key_so_far = key
    
    print(highest_key_so_far)



find_maj_elem(nums)