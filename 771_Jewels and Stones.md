## 题目: 771. Jewels and Stones

***描述***: 字符匹配题目

### Method 1

- **思路**: 两个循环,如果相等,则计数加1

  

- **代码**:

  ```python
  class Solution:
      def numJewelsInStones(self, J, S):
          n = 0
          for j in J:
              for s in S:
                  if j == s:
                      n += 1
       	return n
  ```

  

### Method 2

- **思路**:

  

- **代码**:

  ```python 
  
  ```

  

