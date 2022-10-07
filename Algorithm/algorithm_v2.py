import bisect


def find_closest(number_list: list, target: int) -> int:
    """
    Description:
    ------------
        Function to find the smallest the given target number or the next smallest number

    Parameters:
    ----------

        number_list: List if numbers to search from

        target: integer containing the target number

    Returns:
    -------
        the number
    """
    number_list.sort()
    try:
        i = bisect.bisect_left(number_list, target)
        if i == len(number_list):
            return number_list[i - 1]
        elif number_list[i] == target:
            return number_list[i]
        elif i - 1 < 0:
            return i - 1
        return number_list[i - 1]
    except TypeError:
        return -1