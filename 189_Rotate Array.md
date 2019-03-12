## 题目:  189_Rotate Array

**描述**:  Given an array, rotate the array to the right by k steps

### Method 1

- **思路**: 

  use list ```insert(index, element)``` method

- **代码**:

  ```python
  class Solution:
      def rotate(self, nums, k):
          while k>0:
              nums.insert(0, nums.pop())
              k -= 1
  ```

  

### Method 2

- **思路**:

  旋转后其实是将后面的 k 个元素与前面的进行了交换位置, 所以可以直接交换,不需要一个一个

- **代码**:

  ```python 
  class Solution:
      def rotate(self, nums, k):
          l = len(nums)
          nums[:] = nums[l-k:] + nums[:l-k]
  ```

  

