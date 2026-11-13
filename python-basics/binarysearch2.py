nums = [2, 4, 5, 7, 9, 12]
target = int(input("Search for: "))

low = 0
high = len(nums) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if nums[mid] == target:
        print("Found at index", mid)
        found = True
        break
    elif nums[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Not found")
