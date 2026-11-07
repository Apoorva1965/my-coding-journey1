nums = [4, 9, 2, 7, 5]
target = int(input("Search for: "))

found = False
for i in range(len(nums)):
    if nums[i] == target:
        print("Found at index", i)
        found = True
        break

if not found:
    print("Not found")
