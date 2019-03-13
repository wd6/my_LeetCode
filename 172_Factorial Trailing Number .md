## 题目:  172. Factorial Trailing Num

**描述**: 给一个数，求其阶乘，返回末尾零的个数

### Method 1

- **思路**: iteration 的方法， 只有2*5 会在末尾形成0， 所以是求有几个5的个数

  

- **代码**:

  ```python
  class Solution:
      def trailingZeroes(self, n):
          ans = 0
          while n > 0:
              n = n//5
              ans += n
          return ans
      
  ```

  

### Method 2

- **思路**:

  Recursion

- **代码**:

  ```python 
  class Solution:
      def trailingZeros(self, n):
          return 0 if n == 0 else n//5 + self.trailingZeros(n//5)
  ```

  

