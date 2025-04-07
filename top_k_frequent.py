# LC 347. Top K Frequent Elements : Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

nums = [1,1,1,2,2,3,3,3,3,4]
k = 2
# Expected output: [1,2]

def k_frequent(numlist,frequency):
    frequency_counter = {}
    for num in numlist:
        if num not in frequency_counter:
            frequency_counter[num] = 1
        else:
            frequency_counter[num] += 1
    
    sorted_dict = sorted(frequency_counter)
    print(f"frequency_counter: {frequency_counter}")
    print(f"sorted_dict: {sorted_dict}")


k_frequent(nums,k)