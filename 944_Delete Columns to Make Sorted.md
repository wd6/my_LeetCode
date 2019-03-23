## 题目:  944. Delete Columns to Make Sorted

**描述**：这个题目很难描述

### Method 1

- **思路**: 

  

- **代码**

  ```python
  class Solution:
      def minDeletionSize(self, A):
          ans = 0
          for item in zip(*A):
              if sorted(item) != list(item):
                  ans += 1
         	return ans
  ```

  

### Method 2

- **思路**: 

  

- **代码**

  ```python 
  class Solution:
      def 
  ```

  











