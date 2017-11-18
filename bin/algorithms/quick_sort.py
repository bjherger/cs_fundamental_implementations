def quick_sort(array):
    if len(array) <= 1:
        return array

    quick_sort_helper(array, 0, len(array) - 1)
    return array

def quick_sort_helper(array, lower_index, upper_index):
    if lower_index == upper_index:
        return array

    lower_cursor = lower_index
    upper_cursor = upper_index - 1
    pivot_element = array[upper_index]

    while lower_cursor < upper_cursor:
        if array[lower_cursor] <=pivot_element and array[upper_cursor] > pivot_element:
            lower_cursor += 1
            upper_cursor -= 1
        elif array[lower_cursor] > pivot_element and array[upper_cursor] > pivot_element:
            upper_cursor -= 1
        elif array[lower_cursor] < pivot_element and array[upper_cursor] < pivot_element:
            lower_cursor += 1
        elif array[lower_cursor] > pivot_element and array[upper_cursor] < pivot_element:
            swap(array, lower_cursor, upper_cursor)
            lower_cursor += 1
            upper_cursor -= 1
        else:
            print array[lower_cursor], pivot_element, array[upper_cursor]
            raise ValueError('Issue')

    if pivot_element < array[lower_cursor]:
        swap(array, lower_cursor, upper_index)

    quick_sort_helper(array, lower_index, lower_cursor)
    quick_sort_helper(array, lower_cursor+1, upper_index)
    return array

def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp
    return array
