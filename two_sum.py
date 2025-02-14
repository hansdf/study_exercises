#Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
#You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
#Return the answer with the smaller index first. 

nums = [3,4,7,45,15,35]
target = 10

def two_sum_brute_force(numlist, target): # O(n^2)
    for n1 in range(len(numlist)):
        for n2 in range(len(numlist)):
            if numlist[n1] + numlist[n2] == target:
                print("found at indexes: ", n1, n2)
                return n1, n2

def two_sum_hash(numlist, target): # one pass hashmap = O(n)
    hash_counter = {}
    index = 0
    output_index_list = []
     
    for num in numlist:
        difference = target - num

        if difference in hash_counter:
            print(f"Two sum for target {target} can be found at indexes: ")
            # print(hash_counter[difference], "and", hash_counter[num])
            output_index_list.append(hash_counter[difference])
            output_index_list.append(index)

        if num not in hash_counter:
            hash_counter[num] = index
            index += 1
        
        
        print(output_index_list)

two_sum_hash(nums, target)

# two_sum_brute_force(nums,target)