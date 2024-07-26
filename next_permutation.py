'''

The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, 
then the next permutation of that array is the permutation that follows it in the sorted container. 

If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

'''

# a = [1,1,5]
a = [1,2,3,4]

i = len(a) - 1
f = 0

while i-1>=0:
    
    if a[i-1] < a[i]:
        # print('here')
        # find the num just greater to the right of a[i-1] 
        just_greater = 1e5
        my_idx = 0
        for idx in range(i, len(a)):
            if a[i-1] < a[idx]:
                diff = a[idx] - a[i-1]
                if diff<just_greater and diff > 0:
                    just_greater = diff
                    my_idx = idx
        
        # swap just_greater with a[i-1]
        
        a[i-1], a[my_idx] = a[my_idx], a[i-1]
        
        # now reverse values from i to n
        
        a[i:] = a[i:][::-1]
        
        print(a)
        f = 1
        break
    
    else:
        # print('1111')
        i-=1
if f!=1:
    print(a[::-1])
            
