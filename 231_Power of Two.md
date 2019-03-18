## 题目:  231. Power of Two

**描述**：给一个整数， 检查其是否为2的次方

### Method 1

- **思路**: 

  ``

- **代码**

  ```python
  class Solution:
      def isPowerOfTwo(self, n):
          return n > 0 and bin(n).count('1') == 1
  ```

  

### Method 2

- **思路**: 

  

- **代码**

  ```python 
  class Solution:
      def isPowerOfTwo(self, n):
          return n > 0 and math.log2(n).is_integer()
  ```

  
