
def my_quicksort(list):
    if len(list) == 1:
        return list
    pivot_idx = int((len(list) - 1) / 2)
    had_change = False
    i = 0
    while i < len(list):
        if i < pivot_idx and list[i] > list[pivot_idx]:
            list[pivot_idx], list[i], list[pivot_idx - 1] = list[i], list[pivot_idx - 1], list[pivot_idx]
            pivot_idx = pivot_idx - 1
            had_change = True
        elif i > pivot_idx and list[i] < list[pivot_idx]:
            list[pivot_idx], list[i], list[pivot_idx + 1] = list[i], list[pivot_idx + 1], list[pivot_idx]
            pivot_idx = pivot_idx + 1
            had_change = True
        else:
            i += 1
    if had_change:
        return my_quicksort(list[0:pivot_idx]) + [list[pivot_idx]] + my_quicksort(list[pivot_idx+1:])
    else:
        return list


# list_str = input('Insert list separated by space:')
unsorted_list = [1, 2, 3, 4, 5, 6]  # list_str.split()
sorted_list = my_quicksort(unsorted_list)
print(sorted_list)

unsorted_list = [6, 5, 4, 3, 2, 1]
sorted_list = my_quicksort(unsorted_list)
print(sorted_list)

unsorted_list = [6, 4, 3, 1, 2, 5]
sorted_list = my_quicksort(unsorted_list)
print(sorted_list)

