#Leetcode 5 - brute force algorithm

def longestPalindrome(s: str) -> str:

    lst_of_sub = []
    max_e = ''

    for i in range(len(s)):
        result = ''
        for j in range(i, len(s)):
            result += s[j]
            if result == result[::-1]:
                lst_of_sub.append(result)

    for ele in lst_of_sub:
        if len(ele) > len(max_e):
            max_e = ele
    return max_e

