def find_number(number_list: list, target: int) -> int:
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
    list_min = 0
    list_max = len(number_list) - 1
    middle = 0

    try:
        target = int(target)
        # if the target number is less than the smallest number in the list return -1
        if target < min(number_list):
            return -1

        # if the target number is greater than the smallest number on the list return the highest number in the list
        elif target > number_list[-1]:
            return number_list[-1]

        while list_min <= list_max:

            middle = (list_max + list_min) // 2

            # If target is greater than the middle, set new minimum
            if number_list[middle] < target:
                list_min = middle + 1

            # If the target is less than the middle, set new maximum
            elif number_list[middle] > target:
                list_max = middle - 1

            # means target exists at the middle
            else:
                return number_list[middle]

        # if the target does not exist in the list, subtract from target call the function again
        target -= 1
        return find_number(number_list, target)

    except ValueError:
        return -1