# quick sort implementation
# the pivot will be the starting value on array
# hi = len(array) - 1, lo = 0


def quick_sort (array, hi, lo):
  if lo >= hi:
    return 

  pivot = array[lo]
  pivotIdx = lo

  for i in range (lo, hi + 1):
    # checks how many items are less than the pivot to partition array
    if array[i] < pivot:
      pivotIdx += 1
      array[pivotIdx], array[i] = array[i], array[pivotIdx]

  # moves the pivot
  array[lo], array[pivotIdx] = array[pivotIdx], array[lo]

  # recursive call 
  quick_sort (array, lo, pivotIdx - 1)
  quick_sort (array, pivotIdx + 1, hi)


