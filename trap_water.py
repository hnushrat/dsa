'''
You are given an array non-negative integers heights which represent an elevation map.
Each value heights[i] represents the height of a bar, which has a width of 1.
Return the maximum area of water that can be trapped between the bars.
'''

def trap(height):
    # initialize two lists which hold max height to the left and right of each building

    l_max, r_max = [0 for i in range(len(height))], [0 for i in range(len(height))]
    l_max[0] = height[0] # since leftmost building will not trap water initialize its value to the height of the building
    r_max[-1] = height[-1] # since rightmost ....

        
    # get l_max
    curr_max_l = l_max[0]
    for i in range(1, len(height)):
        curr_max_l = max(curr_max_l, height[i])
        l_max[i] = curr_max_l

    curr_max_r = r_max[-1]
    for i in range(len(height) - 2, -1, -1):
        curr_max_r = max(curr_max_r, height[i])
        r_max[i] = max(curr_max_r, height[i])

    trapped = 0
    '''

    the trapped water above the buildingwill be equal to,
    the the minimum of the heights of the buildings to the left and right of the current building,
    subtracting the current height.

    '''
    for i in range(len(height)):
        trapped+=(min(l_max[i], r_max[i]) - height[i])
        
    return trapped
