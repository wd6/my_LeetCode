## 题目:  414. Third Maximum Number

**描述**：给一组非空的数组，返回第三大的数字，如果第三大不存在，则返回第一大的

### Method 1

- **思路**: 

  记录下当前的最大，第二大和第三大的值，不断更新

- **代码**

  ```python
  class Solution:
      def thirdMax(self, nums):
          first = second = third = -float('inf')
          for n in nums:
              if n == first or n == second or n == third:
                  continue
              elif n > first:
                  third = second
                  second = first
                  first = n
              elif n > second:
                  third = second
                  second = n
              elif n > third:
                  third = i
         	return third if third != -float('inf') else first
  ```

  

### Method 2

- **思路**: 

  利用 collections 里的 Counter() 然后对结果排序

- **代码**

  ```python 
  class Solution:
      def thirdMax(self, nums):
          import collections
          nums = collections.Counter(nums)
          nums = sorted(nums.keys(), reverse=True)
          return nums[2] if len(nums)>2 else nums[0]
  ```

  











