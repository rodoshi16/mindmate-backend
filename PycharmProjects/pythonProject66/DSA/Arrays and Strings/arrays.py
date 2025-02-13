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
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        m = len(word1)
        n = len(word2)

        for i in range(min(m, n)):
            result += word1[i]
            result += word2[i]

        if m < n:
            result += word2[len(word1):]
        else:
            result += word1[len(word2):]

        return result
