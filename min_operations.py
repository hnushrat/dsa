import numpy as np

'''
expected = np.asarray([2,3,2,1])
current = np.asarray([-1,2,3,0])

'''

N = 10
#################################
expected = np.random.randint(1, 11, N)
current = np.random.randint(-3,4, N)
#################################

def find_min_ops(given, target):
    
    diff = target - given # get the difference array

    curr, prev = 0, 0
    operations = 0

    if diff[curr]!=0: # checking for first element of the list
        operations+=abs(diff[curr])
        curr+=1
    
    else: # if zero shift to next index
        curr = 1

    while curr<len(diff):
        # if change of sign, solve for individual element

        if diff[curr]<0 and diff[prev]>0: 
            operations+=abs(diff[curr])
        elif diff[curr]>0 and diff[prev]<0:
            operations+=abs(diff[curr])
        
        # if same sign    
        else:
            if abs(diff[curr])>abs(diff[prev]):
                operations+=(abs(diff[curr]) - abs(diff[prev]))
        curr+=1
        prev+=1
    
    return operations

print(find_min_ops(given = current, target = expected))