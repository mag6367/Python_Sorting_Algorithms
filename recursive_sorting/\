# merge sort python implementation
# time complexity: O(nlog(n))
# note only works with python2

# this function does the recursive merging 
def merge_sort (array, lSide, rSide):
  if rSide > lSide:
    center = (rSide + lSide) / 2
    merge_sort (array, lSide, center)
    merge_sort (array, center + 1, rSide)
    merge_array (array, lSide, rSide, center)  

# this function does the merging
def merge_array (array, lSide, rSide, center):
  # we need to keep track of the two sides we're trying to merge
  firstSide1 = lSide
  lastSide1 = center
  firstSide2 = center + 1
  lastSide2 = rSide

  # create a new list to append the merged valued
  mergedArr = []

  # this is where the merging happens
  while (lastSide1 >= firstSide1) and (lastSide2 >= firstSide2):
    if array[firstSide2] > array[firstSide1]:
      mergedArr.append(array[firstSide1])
      firstSide1 += 1
    else:
      mergedArr.append(array[firstSide2])
      firstSide2 += 1

  while firstSide1 <= lastSide1:
    mergedArr.append(array[firstSide1])
    firstSide1 += 1

  while firstSide2 <= lastSide2:
    mergedArr.append(array[firstSide2])
    firstSide2 += 1

  # this is where we copy the merged array to the given array
  index = lSide
  for i in range (len(mergedArr)):
    array[index] = mergedArr[i]
    index += 1


