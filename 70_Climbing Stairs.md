## 题目:  70. Climbing Stairs

**描述**:  给一个台阶数, 每次只能爬一个台阶或者两个台阶, 那么排上该台阶有多少种方法

### Method 1

- **思路**: 当你站在第 n-1 台阶上时, 走一步的方式到达第 n 个台阶, 当你站在 n-2 个台阶上时, 走两步到达 n 台阶, 此时所有的方法都是不同的(没有 overlap). 所以第 n 个台阶的方式就等于n-1与 n-2 的方式之和

  首先采用递归的方法

- **代码**:

  ```python
  class Solution:
      def climbStairs(self, n):
          if n == 1: return 1
          if n == 2: return 2
          return self.climbStairs(n-1)+self.climbStairs(n-2)
  ```

  

### Method 2

- **思路**: 迭代

  

- **代码**:

  ```python 
  class Solution:
      def climbStairs(self, n):
          if n == 1: return 1
          if n == 2: return 2
          a, b = 2, 1
          for i in range(3, n+1):
              a, b = a+b, a
          return a
              
  ```

  

