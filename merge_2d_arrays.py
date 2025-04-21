# 2570. Merge Two 2D Arrays by Summing Values

nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]
# Output expected: [[1,6],[2,3],[3,2],[4,6]]

def mergeArrays(nums1,nums2):
    counter = {}
    for n1 in nums1:
        #print(n1)
        if n1[0] not in counter:
            counter[n1[0]] = n1[1]

    for n2 in nums2:
        #print(n2)
        if n2[0] not in counter:
            counter[n2[0]] = n2[1]
        elif n2[0] in counter:
            counter[n2[0]] += n2[1]
        
    return_arr = []
    for key in counter:
        print(key,counter[key])
        return_arr.append([key, counter[key]])
    print("return_arr: ", return_arr)
    print("counter: ", counter)
    return sorted(return_arr)


mergeArrays(nums1,nums2)