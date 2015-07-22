# selection sort implementation 
# algorithm: 
# find smallest value
# swap with the first index value
# time complexity: Worst case O(n^2)
# time complexity: Best case O(n)
 	    

def selection_sort (array):
  for i in range (len(array)):
    minVal = array[i] # get this value for comparison
    index = i    # need to keep track of the index 

    # find the minimum value for swapping
    for j in range (i + 1, len(array)):
      if minVal > array[j]: 
        minVal = array[j] 
        index = j

    # finally we do the swap in the array with the element in the current index 
    array[index] = array[i]
    array[i] = minVal

    
      
