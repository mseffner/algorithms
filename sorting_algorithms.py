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
    return a


def shell_sort(a: list):
    return a


def merge_sort(a: list):
    return a


def quick_sort(a: list):
    return a
