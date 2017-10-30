'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''
class Solution(object):
    def twoSum (nums, target):
        dic = {}        
        for ind, num in enumerate(nums):
            if target - num in dic:
                return dic[target-num], ind
            dic[num] = ind
        """
        :type nums: List[int]
        :type target: 
        :rtype: List[int]
        """
print (Solution.twoSum([1,4,3,7],4))
