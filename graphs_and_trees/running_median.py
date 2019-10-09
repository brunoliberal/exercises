# Given a array of numbers, calculate the running median of each o the number added on the list
# Time: O(nlogn) Space: O(n)
def running_median(a):
    min_heap = [None for _ in range(int(len(a) / 2 + 1))]
    min_heap_size = 0
    max_heap = [None for _ in range(int(len(a) / 2 + 1))]
    max_heap_size = 0
    median = ['{:.1f}'.format(a[0])]
    middle_elem = a[0]
    for num in a[1:]:
        if num > middle_elem:  # min heap on right
            insert_minheap(min_heap, num, min_heap_size)
            min_heap_size += 1
        else:  # max heap on left
            insert_maxheap(max_heap, num, max_heap_size)
            max_heap_size += 1

        # if unbalanced
        if min_heap_size > max_heap_size + 1:  # rotate to the left
            # insert maxheap
            insert_maxheap(max_heap, middle_elem, max_heap_size)
            max_heap_size += 1
            # pop minheap
            middle_elem = pop_min_heap(min_heap, min_heap_size)
            min_heap_size -= 1
        elif max_heap_size > min_heap_size + 1:  # rotate to the right
            # insert minheap
            insert_minheap(min_heap, middle_elem, min_heap_size)
            min_heap_size += 1
            # pop maxheap
            middle_elem = pop_max_heap(max_heap, max_heap_size)
            max_heap_size -= 1

        # append median
        if max_heap_size == min_heap_size:
            cur_median = middle_elem
        elif max_heap_size > min_heap_size:
            cur_median = (middle_elem + max_heap[0]) / 2
        else:
            cur_median = (middle_elem + min_heap[0]) / 2
        median.append('{:.1f}'.format(cur_median))
    return median


def insert_minheap(min_heap, num, size):
    min_heap[size] = num
    heapfy_min_up(min_heap, size)


def heapfy_min_up(min_heap, idx):
    parent_idx = (idx - 1) // 2

    if parent_idx < 0:
        return

    if min_heap[parent_idx] > min_heap[idx]:
        min_heap[parent_idx], min_heap[idx] = min_heap[idx], min_heap[parent_idx]
        heapfy_min_up(min_heap, parent_idx)


def insert_maxheap(max_heap, num, size):
    max_heap[size] = num
    heapfy_max_up(max_heap, size)


def heapfy_max_up(max_heap, idx):
    parent_idx = (idx - 1) // 2

    if parent_idx < 0:
        return

    if max_heap[parent_idx] < max_heap[idx]:
        max_heap[parent_idx], max_heap[idx] = max_heap[idx], max_heap[parent_idx]
        heapfy_max_up(max_heap, parent_idx)


def pop_min_heap(min_heap, size):
    head = min_heap[0]
    min_heap[0], min_heap[size - 1] = min_heap[size - 1], None
    heapfy_min_down(min_heap, 0, size - 1)
    return head


def pop_max_heap(max_heap, size):
    head = max_heap[0]
    max_heap[0], max_heap[size - 1] = max_heap[size - 1], None
    heapfy_max_down(max_heap, 0, size - 1)
    return head


def heapfy_min_down(min_heap, idx, size):
    child_idx = 2 * idx + 1

    if child_idx >= size:
        return

    if child_idx + 1 < size and min_heap[child_idx] > min_heap[child_idx + 1]:
        child_idx += 1

    if min_heap[idx] > min_heap[child_idx]:
        min_heap[child_idx], min_heap[idx] = min_heap[idx], min_heap[child_idx]
        heapfy_min_down(min_heap, child_idx, size)


def heapfy_max_down(max_heap, idx, size):
    child_idx = 2 * idx + 1

    if child_idx >= size:
        return

    if child_idx + 1 < size and max_heap[child_idx] < max_heap[child_idx + 1]:
        child_idx += 1

    if max_heap[idx] < max_heap[child_idx]:
        max_heap[child_idx], max_heap[idx] = max_heap[idx], max_heap[child_idx]
        heapfy_max_down(max_heap, child_idx, size)


# print(running_median([12, 4, 5, 3, 8, 7]))

