## 题目:  942. DI String Match

**描述**: 根据字符串的描述增添元素到 list. 

### Method 1

- **思路**:

  

- **代码**:

  ```python
  class Solution:
      def diStringMatch(self, S):
          l, r = 0, len(S)
          ans = []
          for s in S:
              if s == 'I':
                  ans.append(l)
              else:
                  ans.append(r)
       	ans.append(l)
          return ans
  ```


### Method 2

- **思路**:

  

- **代码**:

  ```python 
  
  ```

  

