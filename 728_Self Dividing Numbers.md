## 题目:  728. Self Dividing Numbers

***描述***: 返回能被自身除掉的数

### Method 1

- **思路**:

  

- **代码**:

  ```python
  class Solution:
      def selfDividingNumbers(self, left: 'int', right: 'int') -> 'List[int]':
          res = []
          for num in range(left, right+1):
              for s in str(num):
                  if int(s) == 0 or (num % int(s)) != 0:
                      break
              else:
              	res.append(num)
          return res              
                      
  ```

  







### Method 2

- **思路**:

  

- **代码**:

  ```python 
  
  ```

  

