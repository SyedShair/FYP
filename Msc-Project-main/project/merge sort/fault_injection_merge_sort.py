# Description: Main file for the project of merge sort algorithm with fault injection
# fault: fault is at line 34 a missing k += 1

def merge_sort_func(array):
    if len(array) > 1:  # assert fault here
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort_func(left)
        merge_sort_func(right)

        m = n = p = 0

        while m < len(left) and n < len(right):
            if left[m] < right[n]:
                array[p] = left[m]
                m += 1

            else:
                array[p] = right[n]
                n += 1

            p += 1

        while m < len(left):
            array[p] = left[m]
            m += 1
            p += 1

        while n < len(right):
            array[p] = right[n]
            n += 1

    return array
