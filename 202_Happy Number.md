## 题目:  202. Happy number

**描述**: 一个数字拆开后分别平方并求和，不断重复，如果结果达到1则其实 happy number

### Method 1

- **思路**: 

  

- **代码**:

  ```python
  class Solution:
      def isHappy(self, n):
          repeat = set()
          while n != 1:
              n = sum([int(i)**2 for i in str(n)])
              if n in repeat:
                  return False
              else:
                  repeat.add(n)
        	return True
  ```

  

### Method 2

- **思路**:

  

- **代码**:

  ```python 
  
  ```

  

