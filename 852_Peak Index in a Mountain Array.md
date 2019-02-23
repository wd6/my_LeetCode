## 题目:  852_Peak Index in a Mountain Array

**描述**: 寻找 peak index 

### Method 1

- **思路**: 线性查找

  

- **代码**:

  ```python
  class Solution:
      def peakIndexInMountainArray(self, A):
          for i in range(1,len(a)-1):
              if A[i]>A[i+1]:
                  return i
  ```

  

### Method 2

- **思路**: 二分查找

  

- **代码**:

  ```python 
  class Solution:
      def peakIndexInMountainArray(self, A):
          l, r = 0, len(A)-1
          while l < r:
              m = (l+r) // 2
              if A[m] < A[m+1]:
                  l = m+1
              else:
                  r = m
         	return l
  ```

  

