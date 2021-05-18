def linear_search(list, target):
    '''
       - Return index of the target if found
       - Return None if not found
    '''
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return None
data = [1,2,3,4,5,6,7,8,9,10]
target = 12

print(linear_search(data,target))  #prints None

target = 2
print(linear_search(data,target))  #prints 1
