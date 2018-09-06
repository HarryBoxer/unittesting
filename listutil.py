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

    x = []
    for i in range(0, len(list)):
        if list[i] not in x:
            x.append(list[i])
    return len(x)


print(count_unique(None))
