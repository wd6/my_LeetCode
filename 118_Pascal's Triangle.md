## 题目:  118_Pascal's Traingle

**描述**: 

### Method 1

- **思路**: Dynamic programming

  

- **代码**:

  ```python
  class Solution:
      def generate(self, numRows):
          res, temp = [], [1]
          for n in range(numRows):
              res.append(temp)
              temp = [1] + [temp[k]+temp[k+1] for k in range(n)] + [1]
          return res
  ```

  

### Method 2

- **思路**:

  

- **代码**:

  ```python 
  
  ```

  

