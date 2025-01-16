import math

#Leetcode 2239
def findClosestNumber(nums: list[int]) -> int:
    """
    Find the largest number closest to zero.

    :param nums:
    :return:
    """
    distance = math.inf
    largest_value = 0
    for item in nums:
        if abs(item) - 0 <= distance:
            if item <= 0 and item <= largest_value:
                distance = abs(item)
                largest_value = item
            else:
                if item >= largest_value:
                    distance = abs(item)
                    largest_value = item
    return largest_value
