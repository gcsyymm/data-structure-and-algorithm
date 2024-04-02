def GetMaxOfWindow(nums: list, size: int) -> list:
    """Get the max val of a window of a given list of integers"""
    if not size or size > len(nums):
        return []
    from collections import deque
    queue_of_idx = deque()
    res = []
    for i, num in enumerate(nums):
        if i >= size and i - queue_of_idx[0] > size:
            queue_of_idx.popleft()
        while num > nums[queue_of_idx[-1]]:
            queue_of_idx.pop()
        queue_of_idx.append(i)
        if i >= size - 1:
            res.append(nums[queue_of_idx[0]])
    return res
