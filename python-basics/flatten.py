def flatten(items):
    result = []
    for item in items:
        if isinstance(item, list):       # item is itself a list
            result.extend(flatten(item)) # recursive case
        else:
            result.append(item)          # base case: a plain value
    return result

nested = [1, [2, [3, 4]], 5]
print(flatten(nested))   # [1, 2, 3, 4, 5]
