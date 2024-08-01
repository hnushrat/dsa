'''
Given an integer n, return the number of trailing zeroes in n!.

'''

def get_trailing_zeros(num):
    res = 0
    while num >=5:
        res = res + (num)//5
        num = num//5
    return res

N = 500
print(get_trailing_zeros(N))
