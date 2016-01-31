# Selection Sort Practice

alist = [23, 42, 4, 16, 8, 15]

# 23*, 42**, 4, 16, 8, 15

# 4, 42, 23*, 16, 8, 15



def selectionSortPractice(alist):
    for fill_slot in range(0, len(alist), 1):
        # print(fill_slot)
        # print(alist[fill_slot])
        current_min = 0
        for location in range(1, len(alist), 1):
            if alist[location] < alist[fill_slot]:
                print(location)
                print(alist[location])
                # print(alist[fill_slot])
                current_min = location
                # print(current_min)

        temp = alist[fill_slot]
        alist[fill_slot] = alist[current_min]
        alist[current_min] = temp

print(selectionSortPractice(alist))
