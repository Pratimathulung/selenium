list1 = [1, 3, 5]
list2 = [7, 9, 11, 13, 15]
for a, b in zip(list1, list2):
    if a > b:
        print(a)
    else:
        print(b)
