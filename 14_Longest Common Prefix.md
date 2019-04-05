## 题目: 14. Longest Common Prefix

寻找最长的共有字符串

### Method 1

- **思路**: 此题目要注意所谓的共有是从第一个开始检查,而不是任意位置共有, 比如 $[laa, aal]$, 应该返回"", 而不是 ​$aa$

  

- **代码**

  ```python
  class Solution:
      def LongestCommonPrefix(self, strs):
          if not strs:
              return ""
          for i in range(len(strs[0])):
              for s in strs[1:]:
                  if i >= len(s) or s[i] != strs[0][i]:
                      return strs[0][:i]
          return strs[0]
  ```

  



### Method 2

- **思路**

  

- **代码**

  ```python 
  
  ```

  

