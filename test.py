n_list1 = [1, 2, 3, 4, 5, 6]
n_list2 = [5, 6, 7, 8, 9, 10]
n_list3 = set()

for n1, n2 in zip(n_list1, n_list2):
    # print(n1, n2)
    
    if n1 in n_list1 and n1 in n_list2:
        print("if n1 in both lists reached")
        n_list3.add(n1)

    if n2 in n_list1 and n2 in n_list2:
        print("if n2 in both lists reached")
        n_list3.add(n2)

print(n_list3)