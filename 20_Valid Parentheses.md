## 题目: 20. Valid Parentheses

*tip*: 判断括号的使用是否正确.

### Method 1

- **思路**: 利用 stack 的结构, 判断新加入的是否与 stack 的最末一个构成一对,若构成,则 pop最后一个,否则继续加入

  

- **代码**

  ```python
  class Solution:
      def isValid(s):
          if not s:
              return True
          pairs = ['()', '[]', '{}']
          stack = [s[0]]
          for i in s[1:]:
              if stack:
                  if stack[-1]+i in pairs:
                      stack.pop()
                  else:
                      stack.append(i)
              else:
              	stack.append(i)
          return False if stack else True
  ```

  







### Method 2

- **思路**

  

- **代码**

  ```python 
  
  ```

  

