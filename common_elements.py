# Given two different list of numbers, find what is common between the two
# Receives as inputs two lists > output is a third list containing the common elements between the two

n_list1 = [1, 2, 3, 4, 5, 6]
n_list2 = [5, 6, 7, 8]
    
def find_common(list1, list2):
    n_list3 = set()
    for n1, n2 in zip(n_list1, n_list2):
        if n1 in n_list1 and n1 in n_list2:
            n_list3.add(n1)
        if n2 in n_list1 and n2 in n_list2:
            n_list3.add(n2)
    print(f"Common elements between the two lists are: {n_list3}")

find_common(n_list1, n_list2)