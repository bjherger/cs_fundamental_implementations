def merge_sort(array):
    if len(array) < 2:
        return array
    return merge_sort_helper(array, 0, len(array)-1)


def merge_sort_helper(array, lower_index, upper_index):

    if lower_index == upper_index:
        return [array[lower_index]]

    mid_index = (lower_index + upper_index) / 2
    l = merge_sort_helper(array, lower_index, mid_index)
    r = merge_sort_helper(array, mid_index + 1, upper_index)
    merged = merge(l, r)

    return merged


def merge(l, r):
    l_cursor = 0
    r_cursor = 0
    output = list()

    while len(output) < (len(l) + len(r)):

        if l_cursor >= len(l):
            output.append(r[r_cursor])
            r_cursor += 1
        elif r_cursor >=len(r):
            output.append(l[l_cursor])
            l_cursor +=1
        elif r[r_cursor] <= l[l_cursor]:
            output.append(r[r_cursor])
            r_cursor += 1
        elif l[l_cursor] < r[r_cursor]:
            output.append(l[l_cursor])
            l_cursor += 1
        else:
            raise ValueError('Unknown edge case for merging arrays')

    return output
