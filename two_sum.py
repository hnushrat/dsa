'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

'''
import numpy as np

# a = [-2,-1,1,1,2,3,6]
# a = [1,1,1,1,1,1]

N = 7
target = 10

a = np.random.randint(-2, 10, N)
a = sorted(a)

i, j = 0, len(a) - 1
store = []
while i < j:
    if a[i] + a[j] > target:
        j-=1
    elif a[i] + a[j] < target:
        i+=1
    else:
        while i < j: # remove duplicates from answer
            if a[i] == a[i+1] and (i+1) < j:
                i+=1
            if a[j-1] == a[j] and (j - 1) > i:
                j-=1
            else:
                break
        
        store.append([i, j])
        i+=1
        j-=1
print(store)
