class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if target==nums[i]:
                return i
            elif target<nums[0]:
                return 0
            elif target>nums[-1]:
                return len(nums)
            elif target>nums[i] and target<nums[i+1]:
                return i+1
