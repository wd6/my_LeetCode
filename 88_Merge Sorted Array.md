## 题目:  88. Merge Sorted Array

**描述**：给两个拍好序的数组，返回 merge 两个数组之后的数组1。 只允许在数组一上修改

### Method 1

- **思路**: 不断地比较数组1和2 的最后一个数字，把大的加到 nums1 的最后，然后更新被加过的数组，直到处理完一个数组。可以想象，此时如果 nums1 已经被处理完(m=0), 那就需要把 nums1 前面的缺失补起来，否则就完成了

  

- **代码**

  ```python
  class Solution:
      def merge(self, nums1, m, nums2, n):
          while m > 0 and n > 0:
              if nums1[m-1] > nums2[n-1]:
                  nums1[m+n-1] = nums1[m-1]
                  m -= 1
              else:
                  nums1[m+n-1] = nums2[n-1]
                  n -= 1
       	nums1[:n] = nums2[:n]
  ```

  

### Method 2

- **思路**: 非常巧妙的解法。直接将两个 list 合并然后排序

  

- **代码**

  ```python 
  class Solution:
      def merge(self, nums1, m, nums2, n):
          nums1[m:] = nums2
          nums1.sort()
  ```

  











