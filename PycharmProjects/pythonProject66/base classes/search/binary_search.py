def search(nums: list[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    m = (l + r ) // 2

    while l != r:
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
            m = (l + r) // 2
        else:
            r = m
            m = (l + r) // 2

    if nums[l] == target:
        return l
    else:
        return -1
