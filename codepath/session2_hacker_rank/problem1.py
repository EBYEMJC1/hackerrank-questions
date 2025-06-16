# Given an array arr[], find the first repeating element. The element should occur more than once and the index of its first occurrence should be the smallest.

# Note:- The position you return should be according to 1-based indexing. 

# Examples:

# Input: arr[] = [1, 5, 3, 4, 3, 5, 6]
# Output: 1
# Explanation: 5 appears twice and its first appearance is at index 1 which is less than 3 whose first the occurring index is 2.
# Input: arr[] = [1, 2, 3, 4]
# Output: None
# Explanation: All elements appear only once so answer is None.



# Complete the 'find_min_index_of_repeating' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def find_min_index_of_repeating(arr):
    # Write your code here
    min_index_dict = dict()
    
    for index in range(len(arr)):
        if arr[index] in min_index_dict:
            return min_index_dict[arr[index]]
        else:
            min_index_dict[arr[index]] = index
    return None

