## 题目: 35_Search Insert Position

*tip*: Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

### Method 1

- **思路**: 检查每一个元素,当遇到第一个大于或者等于 target 的元素时候,返回其 index, 就是插入位置. 如果检查到最后都没有大于等于的,那就插入到最后

  

- **代码**

  ```python
  class Solution:
      def searchInsert(self, nums:'list', target:'int'):
          for n in nums:
              if n >= target:
                  return nums.index(n)
          return len(nums)
  ```

  

### Method 2

- **思路**: 二分法, 从中间开始检查. 二分法就是我们每次取出最中间的值进行判断,然后对左右位置进行更新. 就可以以 $log(n)$ 的时间复杂度完成查找

  

- **代码**

  ```python 
  class Solution:
      def searchInsert(self, nums, target):
          left = 0
          right = len(nums)
          while left < right:
              mid = (left+right)//2
              if nums[mid] < target:
                  left = mid + 1
              else:
                  right = mid
         	return left
  ```

  

