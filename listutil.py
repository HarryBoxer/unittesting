def count_unique(list):
    """Count the number of distinct elements in a list.

    The list can contain any kind of elements, including duplicates and nulls in any order.

    (In PyDoc there are different formats for parameters and returns. Use what you prefer.)

    :param list:  list of elements to find distinct elements of
    :return: the number of distinct elements in list

    Examples:
    >>> count_unique(['a','b','b','b','a','c','c'])
    3
    >>> count_unique(['a','a','a','a'])
    1
    >>> count_unique([ ])
    0
    """
    if list is None:
        raise TypeError("List must not be none")
    x = []
    for i in range(0, len(list)):
        if list[i] not in x:
            x.append(list[i])
    return len(x)


def binary_search(list, element):
    """
    This function searches for an element in a list, where the list contents are already sorted
    but this function will sort it again for sure. Use binary search.
    And return index of the matching element if the search element is not in the list will return -1
    :param list: list of elements to find index elements
    :param element: element that interest
    :return: index of that element, -1 if index does not exist.
    >>> binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],5)
    4
    >>> binary_search([90, 91, 1022, 3033, 4000], 91)
    1
    >>> binary_search([90, 91, 1022, 3033, 4000], 999)
    -1
    >>> binary_search(['a', 'b', 'c'], "a")
    0
    >>> binary_search(['b', 'a', 'c'], "a")
    0
    """
    list.sort()
    if list is None:
        raise TypeError("Search element must not be none")
    elif element in list:
        head = 0
        tail = len(list)-1
        while True:
            mid = (head + tail) // 2
            if element == list[mid]:
                return mid
            elif element > list[mid]:
                head = mid + 1
            elif element < list[mid]:
                tail = mid - 1
    else:
        return -1
