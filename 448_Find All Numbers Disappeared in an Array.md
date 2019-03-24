## 题目:  448. Find All Numbers Disappeared in an Array

**描述**：给一个整数数组包含1-n的数字， 有些数字出现两次，有些没有出现，返回那些没有出现的数字

### Method 1

- **思路**: 

  

- **代码**

  ```python
  class Solution:
      def findDisappearedNumber(self, nums):
          return list(set(range(1, len(nums)+1)) - set(nums))
      
  ```

  

### Method 2

- **思路**: 

  

- **代码**

  ```python 
  class Solution:
      def findDisappearedNumber(self, nums):
          n =set(nums)
          return [x for x in range(1, len(nums)+1) if x not in n]
      
  ```

  











