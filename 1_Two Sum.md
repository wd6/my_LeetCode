## 题目:  1. Two Sum

*tips*

### Method 1

- **思路**: 暴力匹配,用两个循环, 时间复杂度是 $O(n^2)$

  

- **代码**

  ```python
  class Soulution1:
      def twoSum(self, nums, target):
          for i in range(0, len(nums)-1):
              for j in range(i+1, len(nums)):
                  if nums[i] == nums[j]:
                      return [i,j]
  ```

  

### Method 2

- **思路**: 将 target-value 的作为键, index 作为值存入字典,然后检查 num[i] 是否在字典中,如果在,则返回 

  

- **代码**

  ```python 
  class Solution2:
      def twoSum(self, nums, target):
          for i in range(len(nums)):
              if nums[i] in adict:
                  return [adict[nums[i]], i]
              adict[target-nums[i]] = i
  ```

  

