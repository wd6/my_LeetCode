## 题目:  674. Longest Continuous Increasing Sub

**描述**: 返回一个 list 里连续的最长子集

### Method 1

- **思路**: 不断增长,那么设置一个当前值, 不断和其进行对比, 如果不增长,则更新该值, 并随时判断改长度是否大于当前最长, 如果大于就,更新最长长度

  

- **代码**:

  ```python
  class Solution:
      def findLengthOfLCIS(self, nums):
          if not nums:
              return 0
          ans ,count = 1, 1 
          cur = nums[0]
          for n in nums[1:]:
              if n > cur:
                  count += 1
              else:
                  count = 1
              cur = n
              ans = max(ans, count)
          return ans
                      
  ```

  

### Method 2

- **思路**:

  

- **代码**:

  ```python 
  
  ```

  

