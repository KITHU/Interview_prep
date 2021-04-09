import math

def merge_sort(arr):
    # check if the array has more than one character
    if len(arr) < 2:
        return arr

    # get the middle of the array
    middle = math.floor(len(arr)/2)
  
    #divid the array into two
    leftarr = arr[0:middle]
    rightarr = arr[middle:len(arr)]
    
    return merge(merge_sort(leftarr),merge_sort(rightarr))


def merge(left, right):
    result = []
    
    # check left and right arr are not empty
    while(len(left) and len(right)):
        #check for smaller element in the two arrays 
        # append smaller element to result and remove if from array
        if left[0] >= right[0]:
            
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    

    while len(left):
        result.append(left.pop(0))

    while len(right):
        result.append(right.pop(0))
    
    return result
arr = [34,8,1,7,6,8]
print("==="*30)
print("unsorted array: ",arr)
print("merge_sort result: ", merge_sort([34,8,1,7,6,8]))
print("==="*30)