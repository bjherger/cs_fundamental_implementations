def quick_sort(array):
    if len(array) <= 1:
        return array

    total = list()
    lower = list()
    upper = list()

    pivot_index = (len(array)-1) / 2

    for elem in array[:pivot_index] + array[pivot_index+1:]:
        if elem <= array[pivot_index]:
            lower.append(elem)
        elif elem > array[pivot_index]:
            upper.append(elem)

    lower_sorted = quick_sort(lower)
    upper_sorted = quick_sort(upper)

    total.extend(lower_sorted)
    total.extend(array[pivot_index])
    total.extend(upper_sorted)


    return total