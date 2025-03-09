# Merge Two Sorted Lists: Given two sorted lists, merge them into one sorted list.

nums1 = [1, 3, 5, 7, 9]
nums2 = [2, 4, 6, 8, 10]

def merge_lists(list1, list2): # very poor optimization, but works
    combined_list = []
    for num in list1:
        combined_list.append(num)

    for num in list2:
        combined_list.append(num)
    
    combined_list.sort()
    print(combined_list)

# merge_lists(nums1, nums2)

def extend_lists(list1, list2):
    list1.extend(list2)
    list1.sort()
    print(list1)


extend_lists(nums1,nums2)