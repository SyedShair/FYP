# Description: binary search algorithm
def binary_search_algo(array, target):
    if len(array) == 0:
        return array
    left = 0
    right = len(array) - 1

    while left <= right:
        midd = (left + right) // 2
        if array[midd] == target:
            return midd
        if array[midd] < target:
            left = midd + 1
        else:
            right = midd - 1
    return -1

