## 题目:  Remove Duplicates from Sorted Array

**描述**: 从一个排好序的 list 中移除重复元素, 但是不能增减额外空间, 使用 in-place $O(1)$

### Method 1

- **思路**:用两个指针,分别是当前元素 和 检查元素, 如果检查的元素和当前元素不相等,那么更新当前元素的下一个索引处的元素为检查元素,最终会保证更新过的元素均为不重复元素. 实际上, 这是一次循环, 有两个指针, 一个不断前行,对 list实现遍历, 另一个用于收集满足条件的元素

  

- **代码**:

  ```python
  class Solution:
      def(self, nums):
          if not nums:
              return 0
          cur = 0
          for i in range(1, len(nums)):
              if nums[i] != nums[cur]:
                  cur += 1
                  nums[cur] = nums[i]
         	return len(nums[:cur+1])
  ```

  

### Method 2

- **思路**:

  

- **代码**:

  ```python 
  
  ```

  

