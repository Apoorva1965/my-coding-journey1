def bsearch(nums, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        return bsearch(nums, target, mid + 1, high)
    return bsearch(nums, target, low, mid - 1)

print(bsearch([2, 4, 5, 7, 9, 12], 9, 0, 5))  # 4
