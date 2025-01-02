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












    # flag = True
    # longest_seq = []
    # for i in range(len(nums) - 1):
    #     if nums[i + 1] < nums[i]:
    #         flag = False
    #     longest_seq.append(nums[i])
    # return len(longest_seq)
