import random

def bubble_sort(arr):
    a, comps = arr[:], 0
    for i in range(len(a) - 1):
        swapped = False
        for j in range(len(a) - 1 - i):
            comps += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a, comps

def selection_sort(arr):
    a, comps = arr[:], 0
    for i in range(len(a) - 1):
        m = i
        for j in range(i + 1, len(a)):
            comps += 1
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
    return a, comps

def binary_search(a, t, lo=0, hi=None, comps=0):   
    if hi is None:
        hi = len(a) - 1
    if lo > hi:
        return -1, comps
    mid = (lo + hi) // 2
    if a[mid] == t:
        return mid, comps + 1
    if t < a[mid]:
        return binary_search(a, t, lo, mid - 1, comps + 1)
    return binary_search(a, t, mid + 1, hi, comps + 1)

print(f"{'n':>6} {'Bubble':>12} {'Selection':>12} {'BinSearch':>10}")
for n in (10, 100, 500, 1000, 2000):
    data = random.sample(range(10 * n), n)
    s1, bc = bubble_sort(data)
    s2, sc = selection_sort(data)
    assert s1 == s2 == sorted(data)   
    _, ssc = binary_search(s1, random.choice(data))
    print(f"{n:>6} {bc:>12,} {sc:>12,} {ssc:>10}")
