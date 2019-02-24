## 题目:  27. Remove Element

**描述**: 移除 nums 里面的的 val 

### Method 1

- **思路**: 不断判断 nums 的每一个元素,  如果等于 val 就移除

  

- **代码**:

  ```python
  class Solution:
      def removeElement(self, nums, val):
          n = 0
          while n < len(nums):
              if nums[n] == val:
                  del nums[n]
              else:
                  n += 1
        	return len(nums)
  ```

  

### Method 2

- **思路**:

  

- **代码**:

  ```python 
  
  ```

  

