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

#Leetcode 1768
class Solution:
    def mergeAlternately(word1: str, word2: str) -> str:
        result = ''
        max_lst= []
        min_lst = []
        max_len = max(len(word1), len(word2))
        for i in range(min(len(word1), len(word2))):
            result += word1[i]
            result += word2[i]

        if len(word1) == max_len:
            max_lst = word1
            min_lst = word2
        else:
            max_lst = word2
            min_lst = word1

        result += max_lst[len(min_lst):]
        return result


