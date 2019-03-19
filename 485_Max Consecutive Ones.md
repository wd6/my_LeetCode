## 题目:  485_Max Consecutive Ones

**描述**：给一个只包含0和1的数组，找出数组中连续1的最大数量

### Method 1

- **思路**: 

  ``

- **代码**

  ```python
  class Solution:
      def findMaxConsecutiveOnes(self, nums):
          maximum, cur = 0, 0
          for n in nums:
              if n == 0:
                  maximum = max(maximum, cur)
                  cur = 0
              else:
                  cur += 1
             	maximum  = max(maximum, cur)
          return maximum
  ```

  

### Method 2

- **思路**: 

  

- **代码**

  

  
