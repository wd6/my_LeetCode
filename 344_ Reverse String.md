## 题目:  344. Reverse String

*描述*: 将一个 list 反向

### Method 1

- **思路**: 用 List reverse()

  

- **代码**:

  ```python
  class Solution:
      def reverseString(s):
          return s.reverse()
      
  """
  return s[::-1]
  """
  ```


### Method 2

- **思路**: 不断交换首位元素

  

- **代码**:

  ```python 
  class Solution:
      def reverseString(s):
          for i in range(len(s)//2):
              s[i], s[-(i+1)] = s[-(i+1)], s[i]
  ```

  

