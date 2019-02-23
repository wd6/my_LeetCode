## 题目:  832. Flipping an Image

**描述**: 将一个二维数组按行翻转, 然后1变0, 0变1

### Method 1

- **思路**: 简单题目

  

- **代码**:

  ```python
  class Solution:
      def flipAndInvertImage(self, A:):
          for i in range(len(A)):
              A[i].reverse()
              for j in range(len(A[i])):
                  A[i][j] = 1-A[i][j]
          return A
  ```

  







### Method 2

- **思路**:

  

- **代码**:

  ```python 
  
  ```

  

