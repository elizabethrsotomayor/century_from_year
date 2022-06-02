import math


def century(year: int) -> int:
    """
    Given a year, return the century it is in.
    :param year:
    :return:
    """
    return math.ceil(year / 100)
