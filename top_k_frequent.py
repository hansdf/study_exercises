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
    
    sorted_dict_value = sorted(frequency_counter.items(), key=lambda x:x[1], reverse=True)

    ans = []

    for key in range(frequency):
        ans.append(sorted_dict_value[key][0])

    return ans

    print(f"frequency_counter: {frequency_counter}")
    print(f"sorted_dict: {sorted_dict_value}")


print(k_frequent(nums,k))