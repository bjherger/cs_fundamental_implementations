def binary_search(sorted_array, query_element):

    if len(sorted_array) < 1:
        return False
    else:
        return binary_search_helper(sorted_array, query_element, 0, len(sorted_array) - 1)


def binary_search_helper(sorted_array, query_element, lower_index, upper_index):
    pivot_index = (lower_index + upper_index) / 2

    if pivot_index > upper_index or pivot_index < lower_index:
        return False

    pivot_value = sorted_array[pivot_index]
    if pivot_value == query_element:
        return True
    elif lower_index == upper_index:
        return False
    elif pivot_value < query_element:
        return binary_search_helper(sorted_array, query_element, pivot_index+1, upper_index)
    elif pivot_value > query_element:
        return binary_search_helper(sorted_array, query_element, lower_index, pivot_index)
