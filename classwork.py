""" 
Given an list nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Example Input: [0,0,11,2,3,4]
Example Output: [11,2,3,4,0,0]
"""

def numbers(num):
    num_list = []
    for digit in num_list:
        if digit == 0:
            num_list.remove(digit)
            num_list.append(digit)
        else:
            pass
result = numbers
numbers()