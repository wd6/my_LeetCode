## 题目: 7. Reverse integer

*tips*

### Method 1

- **思路**: 将 int 输入转换为字符串, 处理完成后再转回 int

  

- **代码**

  ```python
  class Solution:
      def reverse(self, x):
          xstr = str(x)
          stack = []
          new = ""
          
          for s in xstr:
              stack.append(s)
          while stack:
              new += stack.pop()
          
          if x < 0:
              new = "-" + new[:-1]
          intnew = int(new)
          if intnew > 2**31-1 or intnew < (-2)**31:
              return 0
          return intnew
  ```

  

### Method 2

- **思路**: 用 list, 实际上与方法1 差别不大

  

- **代码**

  ```python 
  class Solution:
      def reverse(self, x):
          xlist = list(str(x))
          rev = list(reversed(xlist))
          
          if "-" in rev:
              rev.remove('-')
           
          intrev = int("".join(rev))
          if intrev > 2**31:
              return 0
          if x > 0:
              return intrev
          else:
              return int("-"+"".join(rev))
  ```

  

### Method 3

- **思路** 利用数学计算

  

- **代码**

  ```python
  class Solution:
      def reverse(self, x):
          if x < 0:
              flag = -1
              x = -x
          else:
              flag = 1
              x = x
          result = 0
          while x > 0:
              reminder = x%10
              result = result*10 + reminder
              x = x//10
          return result*flag if result*flag<(2**31-1) and result*flag>-2**31 else 0
  ```

  

  