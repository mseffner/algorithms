"""This program implements various sorting algorithms."""


def bubble_sort(a: list):
    """Bubble Sort works by swapping items in place. Larger items move toward the end of the
    list, and it loops through the list repeatedly until every item is sorted. It is one of the
    least efficient (serious) sorting algorithms.
    O(n^2)
    """
    # Create a copy of the list
    b = a.copy()
    # Get the len of the list
    n = len(b)
    already_sorted = False

    # While there is more than 1 item in the unsorted portion of the list
    while n > 1 and not already_sorted:
        already_sorted = True
        # Loop through the pairs of items in the unsorted portion
        for i in range(n - 1):
            # If the left item in the pair is greater than the right
            if b[i] > b[i + 1]:
                # Swap them
                b[i], b[i + 1] = b[i + 1], b[i]
                already_sorted = False
        # Mark the last item in the list as sorted
        n -= 1

    return b


def selection_sort(a: list):
    """Selection Sort loops through the list slot by slot, and finds the item that needs to go
    into each slot, in order. It is much faster than bubble sort in most cases because it only
    makes 1 swap per pass.
    O(n^2)
    """
    b = a.copy()
    n = len(b)

    # Set the index we are currently trying to fill (left to right)
    index = 0

    while index < n:
        # Assume that the current index is the smallest item left in the list
        smallest_i = index
        smallest = b[smallest_i]
        # Check the rest of the items in the list to the right
        for i in range(index + 1, n):
            # If any of them are smaller
            if b[i] < smallest:
                # Mark it as the smallest item
                smallest = b[i]
                smallest_i = i
        # Swap the current index with the smallest item we found
        b[index], b[smallest_i] = b[smallest_i], b[index]
        # Go to the next index
        index += 1

    return b


def insertion_sort(a: list):
    """Insertion Sort iterates through the list, taking each item and putting it in a sorted
    subsection at the start of the list. To do this, it needs to shift elements to the right
    to make room for the insertion.
    O(n^2)
    """
    b = a.copy()
    n = len(b)

    # Assume the first item in the list is a sorted sub-list and loop through the rest
    for i in range(1, n):
        # Get the next item to be sorted
        to_sort = b[i]
        # Loop backwards through the items of the sorted sub-list
        cursor = i - 1
        while cursor >= 0 and b[cursor] > to_sort:
            # If an item is larger than the current item being sorted, move it to the right
            b[cursor + 1] = b[cursor]
            cursor -= 1
        # Once the proper place has been found, insert the item
        b[cursor + 1] = to_sort

    return b


def shell_sort(a: list):
    """Shell Sort is a modified version of insertion sort. It defines a gap, and treats every
    item in the list that is gap indices apart as being part of a sub-list. It sorts these sub-
    lists before sorting the whole list with a normal insertion sort. By doing multiple passes
    with decreasing gap lengths, the run time is greatly reduced compared to a normal
    insertion sort.
    This implementation uses gaps defined by the formula 2^k - 1, which gives a time complexity
    of O(n^(3/2))"""
    if len(a) <= 1:
        return a

    b = a.copy()
    n = len(b)

    from math import log2
    gaps = [2 ** k - 1 for k in range(1, int(log2(n)) + 1)]

    for gap in reversed(gaps):
        for start in range(gap):
            _shell_helper(b, start, gap)

    return b


def _shell_helper(a: list, start: int, gap: int, end: int=None):
    """This function sorts every gap'th item of the list in place, by way of insertion sort.
    It is used for shell sort."""

    if end is None:
        end = len(a)

    # Assume the first item in the list is a sorted sub-list and loop through the rest
    # Treat the items at every gap'th index as if they were the entire list
    for i in range(start + gap, end, gap):
        # Get the next item to be sorted
        to_sort = a[i]
        # Loop backwards through the items of the sorted sub-list
        cursor = i - gap
        while cursor >= start and a[cursor] > to_sort:
            # If an item is larger than the current item being sorted, move it to the right
            a[cursor + gap] = a[cursor]
            cursor -= gap
        # Once the proper place has been found, insert the item
        a[cursor + gap] = to_sort


def merge_sort(a: list):
    """Merge Sort sorts a list by breaking it down into smaller sub-lists, then sorting those
    sub-lists as it reassembles them.
    O(n log n)
    """
    # The base case: A list of size 1 or 0 is inherently sorted
    if len(a) <= 1:
        return a

    # Break the list in half and sort each half
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    # Merge the two sorted halves back together
    merge_result = []
    i = 0
    j = 0
    # Compare the elements of each half
    while i < len(left) and j < len(right):
        # Append the smaller one to the result
        if left[i] <= right[j]:
            merge_result.append(left[i])
            i += 1
        else:
            merge_result.append(right[j])
            j += 1

    # Append any remaining elements from the left half
    while i < len(left):
        merge_result.append(left[i])
        i += 1

    # Append any remaining elements from the right half
    while j < len(right):
        merge_result.append(right[j])
        j += 1

    return merge_result


def quick_sort(a: list):
    b = a.copy()
    _quick_helper(b, 0, len(b) - 1)
    return b


def _quick_helper(a: list, start: int, end: int):

    if start < end:

        split = _quick_partition(a, start, end)

        if (split - 1) - start < 10:
            _shell_helper(a, start, 1, split)
        else:
            _quick_helper(a, start, split - 1)
        if end - (split + 1) < 10:
            _shell_helper(a, split + 1, 1, end + 1)
        else:
            _quick_helper(a, split + 1, end)


def _quick_partition(a: list, start: int, end: int):

    mid = (start + end) // 2
    # Sort the first, last, and mid items so that the mid is the median
    if a[start] > a[end]:
        _swap(a, start, end)
    if a[start] > a[mid]:
        _swap(a, start, mid)
    if a[mid] > a[end]:
        _swap(a, mid, end)

    pivot = mid
    left = start
    right = end

    done = False

    # While the left and right pointers have not crossed
    while not done:
        # Move the left pointer to the right until it either crosses the right pointer
        # or it finds a value greater than the pivot
        while left <= right and a[left] <= a[pivot]:
            left += 1

        # Move the right pointer to the left until it either crosses the left pointer
        # or it finds a value less than the pivot
        while right >= left and a[right] >= a[pivot]:
            right -= 1

        # If the pointers crossed, we're done
        if right < left:
            done = True
        # If they didn't cross yet, swap the two values
        else:
            _swap(a, left, right)
    # Swap the pivot with the correct pointer
    if right < pivot:
        _swap(a, left, pivot)
        split = left
    else:
        _swap(a, right, pivot)
        split = right

    return split


def _swap(a, l, r):
    a[l], a[r] = a[r], a[l]
