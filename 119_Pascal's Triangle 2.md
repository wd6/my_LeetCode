## 题目:  119. Pascal's triangle 2

**描述**：杨辉三角的第n行的值

### Method 1

- **思路**: 记录下前一行的值，下一行的值既可以推算

  

- **代码**

  ```python
  class Solution:
      def getRow(self, rowIndex):
          pre = [1, 1]
          row = [1 for i in range(rowIndex+1)]
          for i in range(2, rowIndex+1):
              row = [1 for x in range(i+1)]
              for j in range(1, i):
                  row[j] = pre[j-1] + pre[j]
             	pre = row
          return row
  ```

  

### Method 2

- **思路**: 直接不断更新 row, 实际上每一个值都等于当前值加上前一个值

  

- **代码**

  ```python 
  class Solution:
      def getRow(self, rowIndex):
          row = [1 for i in range(rowIndex+1)]
          for i in range(2, rowIndex+1):
              for j in range(i-1, 0, -1 ):
                  row[j] = row[j] + row[j-1]
        	return row
  ```

  











