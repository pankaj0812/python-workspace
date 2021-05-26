"""
    Implementing Binary Search In Python.
    For binary search, the inputs has to be sorted. Binary search eliminates 50% of the input in every iteration

    @author: Amitesh Kumar
"""

import random
from typing import List, Any

def binary_search_iterative(elements: List, element: Any):
    """
    Search for the given element in the list of elements using binary search

    Args:
        elements (List): The list of elements
        element (Any): The element to search in the list of elements

    Returns:
        [int]: The index of the element in the list of elements
    """

    index = -1
    start = 0
    end = len(elements) -1

    while start <= end:
        middle = (start + end) // 2

        if elements[middle] == element:
            index = middle
        elif elements[middle] > element:
            end = middle - 1
        else:
            start = middle + 1

        if index != -1:
            break
    return index


def binary_search_recursive(elements: List, element: Any, start: int, end: int):
    """

    Args:
        elements (List): [description]
        element (Any): [description]

    Returns:
        [type]: [description]
    """

    if start <= end:
        middle = (start + end) // 2
        if elements[middle] == element:
            return middle
        elif elements[middle] > element:
            end = middle
            return binary_search_recursive(elements, element, start, end)
        else:
            start = middle
            return binary_search_recursive(elements, element, start, end)
    else:
        return -1

if __name__ == '__main__':
    print("Binary Search In Python")

    MIN_SIZE = 0
    MAX_SIZE = 1024
    inputs = [i for i in range(MIN_SIZE, MAX_SIZE)]
    rand_input = random.randint( MIN_SIZE, MAX_SIZE)

    print("Iterative Approach")
    input_index = binary_search_iterative(inputs, rand_input)
    print(f"Input element: {rand_input} | Input index: {input_index}")

    print("\nRecursive Approach")
    input_index = binary_search_recursive(inputs, rand_input, 0, len(inputs))
    print(f"Input element: {rand_input} | Input index: {input_index}")
