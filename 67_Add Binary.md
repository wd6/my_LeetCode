## 题目:  67. Add Binary

**描述**: 将两个二进制相加并返回二进制

### Method 1

- **思路**:  二进制是字符串的形式, 用 int(b, 2) 可将其转换成 10进制, 然后相加再转为二进制. 要注意, bin() 转成的二进制以0b开头, 要去掉0b

  

- **代码**:

  ```python
  class Solution:
      def (self, a, b):
          return bin(int(a,2)+int(b,2))[2:]
  ```

  

### Method 2

- **思路**:

  

- **代码**:

  ```python 
  
  ```

  

