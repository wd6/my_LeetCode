## 题目:  581. Shortest Unsorted Continuous Subarray

**描述**：给一个整数数组， 找出一个连续的 subarray 使得对这个 subarray 排序之后，整个数组变恢复秩序。返回 subarray 的长度

### Method 1

- **思路**: 先对数组进行排序，然后对比排序的数组和原数组，就可以得出 subarray

  

- **代码**

  ```python
  class Solution:
      def findUnsortedSubarray(self, nums):
          l = len(nums)
          r = 0
          sorted_nums = sorted(nums)
          for i in range(len(nums)):
              if nums[i] != sorted_nums[i]:
                  l = min(l, i)
              	r = max(r, i)
         	return r-l+1 if r-l>0 else 0
  ```

  

### Method 2

- **思路**:  用 stack

  

- **代码**

  ```python 
  class Solution:
      def findUnsortedSubarray(self, nums):
          stack = []
          l = len(nums)
          r = 0
          for i in range(len(nums)):
              while stack and nums[stack[-1]] > nums[i]:
                  l = min(l, stack.pop())
              stack.append(i)
          stack = []
          for i in range(len(nums)-1, -1, -1):
              while stack and nums[stack[-1]] < nums[i]:
                  r = max(r, stack.pop())
              stack.append(i)
          return r-l+1 if r-l>0 else 0
          
  ```

  
