list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]
list3 = [2, 4, 6, 8]

# Check if element exists in all lists
result = [x for x in list1 if x in list2 and x in list3]

print("Common elements:", result)