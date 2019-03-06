## 题目:  53. Maximum Subarray

**描述**:  给一个整数的数组, 找出具有最大的和的连续 subarray

### Method 1

- **思路**: 

  

- **代码**:

  ```python
  class Solution:
      def maxSubArray(self, nums):
          curSum, maxSum = nums[0], nums[0]
          for n in nums[1:]:
              curSum += n
              curSum = max(curSum, n)
              maxSum = max(maxSum, curSum)
         	return maxSum
  ```


### Method 2

- **思路**:

  

- **代码**:

  ```python
  def maxSubArray(self, nums):
      for i in range(1, len(nums)):
          if nums[i-1] > 0:
              nums[i] += nums[i-1]
    	return max(nums)
  ```

  

  

