# Selection Sort
# Goal: Divide list into two portopns, 1. sorted 2. unsorted
# How? 1 item is moved from the unsorted to the sorted

alist = [23, 42, 4, 16, 8, 15]

# find minimum unsorted element
# use index[0] as the assumed smallest element
# compare each following element to the assumed smallest
# once the smallest is found put it at the beginning of list

# after_one_iteration = [4, 42, 23, 16, 8, 15]
#
# after_second_iteration = [4, 8, 23, 16, 42, 15]
#
# after_third_iteration = [4, 8, 23, 16, 42, 15]
#
# after_fourth_iteration = [4, 8, 15, 16, 42, 23]
#
# after_fifth_iteration = [4, 8, 15, 16, 23, 42]


# Sort backwards
# Sort forwards
# Describe in detail what happened

def selectionSortBackwards(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionofMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionofMax] = temp


def selectionSortForwards(alist):
    for fillslot in range(0, len(alist), 1):
        positionOfMax = 0
        for location in range(1, len(alist) - 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
