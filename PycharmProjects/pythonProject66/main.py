def lengthOfLIS(nums) -> int:
    """

    >>> lengthOfLIS([10,9,2,5,3,7,101,18])
    7
    >>> lengthOfLIS([[0,1,0,3,2,3]])
    5
    >>> lengthOfLIS([7,7,7,7,7,7,7])
    1

    """

    long_seq = []
    seq = []
    for i in range(len(nums) - 1):
        if nums[i] < nums[i+1] and nums[i] not in seq:
            seq.append(nums[i])
            seq.append(nums[i+1])
            if len(seq) > len(long_seq):
                long_seq = seq
        else:
            seq = []

    return len(long_seq)


def transpose(matrix):

    total = len(matrix[0]) + len(matrix)
    col_diff = total - len(matrix[0])
    row_diff = total - len(matrix)

    for i in range(len(matrix)):
        for k in range(col_diff):
            matrix[i].append(0)

        for j in range(len(matrix)):
            for m in range(row_diff):
                matrix[j].append(0)

    return matrix

# Leetcode 997 using Two pointer approach
def sortedSquares(nums: list[int]) -> list[int]:
    left = 0
    right = len(nums) - 1
    result = []

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result.append(nums[left] ** 2)
            left += 1
        else:
            result.append(nums[right] ** 2)
            right -= 1

    result.reverse()
    return result


#234 Palindrome Linked List
def isPalindrome(head: [ListNode]) -> bool:
    curr = head
    lst = []
    while curr is not None:
        lst.append(curr.val)
        curr = curr.next
    return lst[::-1] == lst
