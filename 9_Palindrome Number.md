## 题目:  9. Palindrome number

*tips*

### Method 1

- **思路**: 将数字转为 list, 用pop 取 list 的最后与前面进行对比

  

- **代码**

  ```python
  class Solution:
      def isPalindrome(self, x: 'int') -> 'bool':
          if x<0:
              return False
          xlist = list(str(x))
  
          if len(xlist)%2 == 0:
              for i in range(len(xlist)//2):
                  if xlist[i] != xlist.pop():
                      return False
              return True
          else:
              for i in range((len(xlist)-1)//2):
                  if xlist[i] != xlist.pop():
                      return False
              return True
  ```

  

### Method 2

- **思路** 直接用 str 的 反向: <code>str[::-1]</code>

  

- **代码**

  ```python 
  class Solution:
      def isPalindrome(self, x):
          return str(x) == str(x)[::-1]
  ```

  

