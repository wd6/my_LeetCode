## 题目:  747. Largest Number At Least Twice of Others

**描述**：给一个数组，若其最大的数比其他的数都要大2倍及以上，返回该数的 index， 否则返回-1

### Method 1

- **思路**: 

  

- **代码**

  ```python
  class Solution:
      def dominantIndex(self, nums):
          m = max(nums)
          if all(m >= 2*x for x in nums if x!=m):
              return nums.index(m)
          else:
              return -1
  ```

  

### Method 2

- **思路**: 

  

- **代码**

  ```python 
  class Solution:
      def 
  ```

  
