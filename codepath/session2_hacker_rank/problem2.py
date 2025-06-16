# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and must be in ascending order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Explanation: [4,9]

#
# Complete the 'intersection' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums1
#  2. INTEGER_ARRAY nums2
#

def intersection(nums1, nums2):
    # Write your code here
    set1 = set(nums1)
    set2 = set(nums2)
    return sorted(list(set1 & set2))