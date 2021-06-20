def binary_search(target, list):
    '''
       Interactive binary search method
       Binary search run in constant space
       and logarithmic time
    '''

    first_index = 0
    last_index = len(list) - 1
    

    while( first_index <= last_index):
        mid = (first_index + last_index)//2

        if list[mid] == target:
            return mid
        elif list[mid] > target:
            last_index = mid-1
        else:
            first_index = mid+1

    return None


data = [1,2,3,4,5,6,7,8,9,10]
target = 13

i = binary_search(target,data)
print(i) 
